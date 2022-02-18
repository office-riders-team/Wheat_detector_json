# USE ONLY IN NOTEBOOKS WHILE TRAINING THE MODELS

import cpuinfo
import torch
from torch.cuda.amp import autocast
import numpy as np
import cv2
import effdet
from dataset import Dataset



def get_device_name(device):
    def get_cpu():
        cpu_info = cpuinfo.get_cpu_info()
        device_name = cpu_info["brand_raw"]
        device_type = "CPU"
        
        return device_name, device_type
    
        
    if "cuda" in device:
        if torch.cuda.is_available():
            device_name = torch.cuda.get_device_name(device)
            device_type = "GPU"
        else:
            device_name, device_type = get_cpu()
    else:
        device_name, device_type = get_cpu()
        
    name = f"{device_name} ({device_type})"
    return name


def transform_bounding_boxes(bounding_boxes, source_format="pascal_voc", target_format="pascal_voc"):
    transformed_bounding_boxes = []
    for bounding_box in bounding_boxes:
        transformed_bounding_box = transform_bounding_box(bounding_box, source_format=source_format, target_format=target_format)
        transformed_bounding_boxes.append(transformed_bounding_box)
        
    transformed_bounding_boxes = np.array(transformed_bounding_boxes)
    return transformed_bounding_boxes
        

def transform_bounding_box(bounding_box, source_format="pascal_voc", target_format="pascal_voc"):
    methods = {
        "pascal_voc": from_pascal_voc,
        "coco": from_coco,
        "yolo": from_yolo,
    }
    
    from_method = methods.get(source_format, from_pascal_voc)
        
    transformed_bounding_box = from_method(bounding_box=bounding_box, target_format=target_format)
        
    return transformed_bounding_box
        

def from_pascal_voc(bounding_box, target_format="pascal_voc"):
    x_min, y_min, x_max, y_max = bounding_box
        
    width = x_max - x_min
    height = y_max - y_min
        
    half_width = width / 2
    half_height = height / 2
        
    if target_format == "coco":
        formated_bounding_box = [x_min, y_min, width, height]
            
    elif target_format == "yolo":
        x_center = x_max / 2
        y_center = y_max / 2
            
        formated_bounding_box = [x_center, y_center, width, height]
            
    else:
        formated_bounding_box = bounding_box
            
    formated_bounding_box = np.array(formated_bounding_box).round()
        
    return formated_bounding_box
        
def from_coco(bounding_box, target_format="pascal_voc"):
    x_min, y_min, width, height = bounding_box 
        
    x_max = x_min + width
    y_max = y_min + height
        
    if target_format == "pascal_voc":
        formated_bounding_box = [x_min, y_min, x_max, y_max]
            
    elif target_format == "yolo":
        x_center = x_max / 2
        y_center = y_max / 2
            
        formated_bounding_box = [x_center, y_center, width, height]
            
    else:
        formated_bounding_box = bounding_box
            
    formated_bounding_box = np.array(formated_bounding_box).round()
        
    return formated_bounding_box
    

def from_yolo(bounding_box, target_format="pascal_voc"):
    x_center, y_center, width, height = bounding_box
        
    half_width = width / 2
    half_height = height / 2
        
    x_max = x_center + half_width
    x_min = x_center - half_width
    y_max = y_center + half_height
    y_min = y_center - half_height
        
    if target_format == "pascal_voc":
        formated_bounding_box = [x_min, y_min, x_max, y_max]
            
    elif target_format == "coco":
        formated_bounding_box = [x_min, y_min, width, height]
        
    else:
        formated_bounding_box = bounding_box
            
    return formated_bounding_box


def draw_bboxes(image, bboxes, source_format="pascal_voc", color=(0, 255, 255), thickness=1):
    methods = {
        "pascal_voc": from_pascal_voc,
        "coco": from_coco,
        "yolo": from_yolo,
    }
    
    image_with_bboxes = image.copy()
    for bbox in bboxes:
        from_method = methods.get(source_format, from_pascal_voc)
        bbox = from_method(bounding_box=bbox, target_format="pascal_voc")
        x_min, y_min, x_max, y_max = bbox.round().astype(int)
        image_with_bboxes = cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)
        
    return image_with_bboxes


def save_checkpoint(model, optimizer, epoch=None, loss=None, path="checkpoint.pth"):
    checkpoint = {
        "model_state": model.state_dict(),
        "optimizer_state": optimizer.state_dict(),
        "epoch": epoch,
        "loss": loss
    }
    
    torch.save(checkpoint, path=path)
    
    return checkpoint


def create_model(model_name="tf_efficientdet_d0", num_classes=1, pretrained=True, image_size=(512, 512), checkpoint_path=None, mode="train"):
    config = effdet.get_efficientdet_config(model_name)
    config.image_size = image_size
    config.num_classes = num_classes
    config.norm_kwargs=dict(eps=.001, momentum=.01)

    model = effdet.EfficientDet(config, pretrained_backbone=pretrained)
    model.class_net = effdet.efficientdet.HeadNet(config, num_outputs=config.num_classes)

    if checkpoint_path is not None:
        if torch.cuda.is_available():
            checkpoint = torch.load(checkpoint_path)
        else:
            checkpoint = torch.load(checkpoint_path, map_location="cpu")
        
        model.load_state_dict(checkpoint)            
        print(f"Loaded checkpoint from '{checkpoint_path}'")
    
    
    if mode == "inference":
        model = effdet.DetBenchPredict(model, config)
    else:
        model = effdet.DetBenchTrain(model, config)
        
    return model


def train_one_batch(batch, model, optimizer, scaler=None, clipping_norm=None, inputs_device="cpu", targets_device="cpu"):
    optimizer.zero_grad()
    
    if scaler is not None:
        with autocast():
            inputs, targets = Dataset.collate_batch(batch, inputs_device=inputs_device, targets_device=targets_device)
            outputs = model(inputs, targets)

            batch_loss = outputs["loss"]

        scaler.scale(batch_loss).backward()
        
        if clipping_norm is not None:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=clipping_norm)
        
        scaler.step(optimizer)
        scaler.update()
    else:
        inputs, targets =  Dataset.collate_batch(batch, inputs_device=inputs_device, targets_device=targets_device)
        outputs = model(inputs, targets)
        
        batch_loss = outputs["loss"]
        
        batch_loss.backward()
        if clipping_norm is not None:
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=clipping_norm)
            
        optimizer.step()
        
    return batch_loss


def validate(model, loader, inputs_device="cpu", targets_device="cpu"):
    loss = 0
    with torch.no_grad():
        for batch in loader:
            inputs, targets = Dataset.collate_batch(batch, inputs_device=inputs_device, targets_device=targets_device)
            outputs = model(inputs, targets)

            batch_loss = outputs["loss"]
            loss += batch_loss
        
    loss /= len(loader)
    
    return loss
