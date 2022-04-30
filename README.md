# Orchid_Classification

## Getting the code
You can download all the files in this repository by cloning this repository:  
```
git clone https://github.com/Jia-Wei-Liao/Orchid_Classification.git
```

## Training
To train the model, you can run this command:
```
python train.py -bs <batch size> \
                -ep <epoch> \
                --model <model> \
                --pretrain <using pretrained-weight> \
                --img_size <crop and resize to img_size> \
                --loss <loss function> \
                --optim <optimizer> \
                --lr <learning rate> \
                --weight_decay <parameter weight decay> \
                --scheduler <learning rate schedule> \
                --autoaugment <use autoaugmentation> \
                --rot_degree <degree of rotation> \
                --fliplr <probabiliy of horizontal flip> \
                --noise <probabiliy of adding gaussian noise> \
                --num_workers <number worker> \
                --device <gpu id> \
                --seed <random seed>
```
- model: EfficientB4, Swin
- loss: CE, MCCE, FL, FLSD
- optim: SGD, Adam, AdamW, Ranger
- scheduler: step (gamma, step_size), cos

### For EfficientNet_b4 with MCCE loss
```
python train.py --model EfficientB4 --img_size 416 --loss MCCE
```

### For Swin Transformer
```
python train.py --model Swin --pretrain 1 --img_size 384 -bs 64 --lr 3e-4
```


## Testing
To test the results, you can run this command:
```
python test.py --checkpoint <XX-XX-XX-XX-XX> --weight <ep=XXXX-acc=0.XXXX.pth>
```


## Experiment results
Before training, we use RandomResizedCrop(416), RandomHorizontalFlip(p=0.5), RandomRotation(degree=10), Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)), RandomNoise(p=0.1) and Autoaugmentation as preprocessing.

<table>
  <tr>
    <td>checkpoint</td>
    <td>model</td>
    <td>bs</td>
    <td>epochs</td>
    <td>loss</td>
    <td>optimizer</td>
    <td>scheduler</td>
    <td>val acc</td>
    <td>test acc</td>
  </tr>
  <tr>
    <td>04-11-23-42-37</td>
    <td>EfficientNet-b4</td>
    <td>16</td>
    <td>200</td>
    <td>CE</td>
    <td>AdamW (lr=1e-3)</td>
    <td>Step</td>
    <td>0.8630</td>
    <td> </td>
  </tr>
  <tr>
    <td>04-11-23-58-50</td>
    <td>EfficientNet-b4</td>
    <td>16</td>
    <td>200</td>
    <td>MCCE</td>
    <td>AdamW (lr=1e-3)</td>
    <td>Step</td>
    <td>0.8584</td>
    <td> </td>
  </tr>
  <tr>
    <td>04-12-00-14-06</td>
    <td>EfficientNet-b4</td>
    <td>32</td>
    <td>200</td>
    <td>FLSD</td>
    <td>AdamW (lr=1e-3)</td>
    <td>Step</td>
    <td>0.8607</td>
    <td> </td>
  </tr>
  <tr>
    <td>04-12-00-14-06</td>
    <td>EfficientNet-b4</td>
    <td>32</td>
    <td>200</td>
    <td>FLSD</td>
    <td>AdamW (lr=5e-3)</td>
    <td>Step</td>
    <td>0.8402</td>
    <td> </td>
  </tr>
  <tr>
    <td>04-12-01-49-02</td>
    <td>EfficientNet-b4</td>
    <td>32</td>
    <td>200</td>
    <td>CE</td>
    <td>AdamW (lr=1e-3)</td>
    <td>Step</td>
    <td>0.8402</td>
    <td> </td>
  </tr>
  <tr>
    <td>04-12-02-08-09</td>
    <td>EfficientNet-b4</td>
    <td>8</td>
    <td>200</td>
    <td>CE</td>
    <td>AdamW (lr=1e-3)</td>
    <td>Step</td>
    <td>0.8447 </td>
    <td> </td>
  </tr>
  <tr>
    <td>04-12-02-09-10</td>
    <td>EfficientNet-b4</td>
    <td>16</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=1e-3)</td>
    <td>Step</td>
    <td>0.8699 </td>
    <td> </td>
  </tr>
  <tr>
    <td>04-12-02-19-38</td>
    <td>EfficientNet-b4</td>
    <td>16</td>
    <td>200</td>
    <td>FLSD</td>
    <td>AdamW (lr=1e-3)</td>
    <td>Step</td>
    <td>0.8470 </td>
    <td> </td>
  </tr>
  <tr>
    <td>04-12-16-01-10</td>
    <td>Swin</td>
    <td>32</td>
    <td>200</td>
    <td>CE</td>
    <td>AdamW (lr=3e-4)</td>
    <td>Step</td>
    <td>0.8927 </td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-13-19-57-43</td>
    <td>Swin</td>
    <td>32</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=3e-4)</td>
    <td>Step</td>
    <td>0.9110 </td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-13-19-57-43</td>
    <td>Swin</td>
    <td>64</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=3e-4)</td>
    <td>Step</td>
    <td>0.9110</td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-19-13-58-40</td>
    <td>ConvB</td>
    <td>64</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=3e-4)</td>
    <td>Step</td>
    <td>0.8836</td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-19-21-12-43</td>
    <td>ConvB</td>
    <td>64</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=3e-4)</td>
    <td>Step</td>
    <td>0.8699</td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-19-21-12-43</td>
    <td>ConvB</td>
    <td>64</td>
    <td>200</td>
    <td>FLSD</td>
    <td>AdamW (lr=3e-4)</td>
    <td>Step</td>
    <td>0.8836</td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-27-17-28-28</td>
    <td>CSwin</td>
    <td>32</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=3e-5)</td>
    <td>Step</td>
    <td>0.8676</td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-27-19-58-18</td>
    <td>CSwin</td>
    <td>32</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=1e-4)</td>
    <td>Step</td>
    <td>0.8858</td>
    <td> - </td>
  </tr>
  <tr>
    <td>04-27-21-12-57</td>
    <td>CSwin</td>
    <td>32</td>
    <td>200</td>
    <td>FL</td>
    <td>AdamW (lr=8e-5)</td>
    <td>Step</td>
    <td>0.8744</td>
    <td> - </td>
  </tr>
<table>

## GitHub Acknowledgement
We thank the authors of these repositories:
- MCCE: https://github.com/Kurumi233/Mutual-Channel-Loss  
- FLSD: https://github.com/torrvision/focal_calibration  
- Ranger21: https://github.com/lessw2020/Ranger21  
- AutoAugment: https://github.com/DeepVoltaire/AutoAugment  


## Citation
```
@misc{
    title  = {orchid_classification},
    author = {Jia-Wei Liao, Yu-Hsi Chen, Jing-Lun Huang, Kuok-Tong Ng},
    url    = {https://github.com/Jia-Wei-Liao/Orchid_Classification},
    year   = {2022}
}
```
