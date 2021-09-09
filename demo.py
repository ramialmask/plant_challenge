import matplotlib.pyplot as plt
import preprocessing
import cv2


path = "/home/rami/Documents/Promotion/H³ Hackathon/plant challenge/LCC2020/train_images/"
plant_path = f"{path}A3_plant026_rgb.png"

plant_image = cv2.imread(plant_path)
fig, axes = plt.subplots(nrows = 2, ncols = 4)
axes[0,3].imshow(plant_image)
axes[1,3].imshow(plant_image)

gs_ = preprocessing.green_dominance(plant_image)

axes[0,0].imshow(plant_image[:,:,0])
axes[0,1].imshow(plant_image[:,:,1])
axes[0,2].imshow(plant_image[:,:,2])

axes[1,0].imshow(plant_image[:,:,0] * gs_)
axes[1,1].imshow(plant_image[:,:,1] * gs_)
axes[1,2].imshow(plant_image[:,:,2] * gs_)


plt.show()
