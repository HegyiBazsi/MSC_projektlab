# I M P O R T   L I B R A R I E S
import numpy as np
import cv2
import random
import os.path
import time


# Function that contains the location of the files
def locations():
    # I N P U T
    locations.inputImageDir = ""
    locations.inputImageDirCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\original\\circle\\"
    locations.inputImageDirElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\original\\else\\"
    locations.inputImageDirStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\original\\star\\"
    locations.inputImageDirSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\original\\square\\"

    # O U T P U T
    locations.outputCleanUp = ""

    # Clean up
    locations.outputCleanUpElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\cleanUp" \
                            "\\else\\cleanUpElse{:>03}.jpg"
    locations.outputCleanUpCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\cleanUp" \
                             "\\circle\\cleanUpCircle{:>03}.jpg"
    locations.outputCleanUpStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\cleanUp" \
                                  "\\star\\cleanUpStar{:>03}.jpg"
    locations.outputCleanUpSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\cleanUp" \
                                    "\\square\\cleanUpSquare{:>03}.jpg"

    # Rotate
    locations.outputRotate = ""
    locations.outputRotateElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\rotate" \
                       "\\else\\rotateElse{:>03}.jpg"
    locations.outputRotateCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\rotate" \
                        "\\circle\\rotateCircle{:>03}.jpg"
    locations.outputRotateStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\rotate" \
                                 "\\star\\rotateStar{:>03}.jpg"
    locations.outputRotateSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\rotate" \
                                   "\\square\\rotateSquare{:>03}.jpg"

    # Translation
    locations.outputTranslation = ""
    locations.outputTranslationElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\translation" \
                           "\\else\\translationElse{:>03}.jpg"
    locations.outputTranslationCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\translation" \
                            "\\circle\\translationCircle{:>03}.jpg"
    locations.outputTranslationStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\translation" \
                                      "\\star\\translationStar{:>03}.jpg"
    locations.outputTranslationSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\translation" \
                                        "\\square\\translationSquare{:>03}.jpg"

    # Affine
    locations.outputAffineTransformation = ""
    locations.outputAffineTransformationElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                         "affineTransformation\\else\\affineTransformationElse{:>03}.jpg"
    locations.outputAffineTransformationCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                          "affineTransformation\\circle\\affineTransformationCircle{:>03}.jpg"
    locations.outputAffineTransformationStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                               "affineTransformation\\star\\affineTransformationStar{:>03}.jpg"
    locations.outputAffineTransformationSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                                 "affineTransformation\\Square\\affineTransformationSquare{:>03}.jpg"

    # Perspective
    locations.outputPerspectiveTransformation = ""
    locations.outputPerspectiveTransformationElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                         "perspectiveTransformation\\else\\perspectiveTransformationElse{:>03}.jpg"
    locations.outputPerspectiveTransformationCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                          "perspectiveTransformation\\circle\\perspectiveTransformationCircle{:>03}.jpg"
    locations.outputPerspectiveTransformationStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                                    "perspectiveTransformation\\star\\" \
                                                    "perspectiveTransformationStar{:>03}.jpg"
    locations.outputPerspectiveTransformationSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                                      "perspectiveTransformation\\square\\" \
                                                      "perspectiveTransformationSquare{:>03}.jpg"

    # Brightness Up
    locations.outputBrightnessUp = ""
    locations.outputBrightnessUpElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                              "brightnessUp\\else\\brightnessUpElse{:>03}.jpg"
    locations.outputBrightnessUpCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                               "brightnessUp\\circle\\brightnessUpCircle{:>03}.jpg"
    locations.outputBrightnessUpStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                       "brightnessUp\\star\\brightnessUpStar{:>03}.jpg"
    locations.outputBrightnessUpSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                         "brightnessUp\\square\\brightnessUpSquare{:>03}.jpg"

    # Brightness Down
    locations.outputBrightnessDown = ""
    locations.outputBrightnessDownElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                 "brightnessDown\\else\\brightnessDownElse{:>03}.jpg"
    locations.outputBrightnessDownCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                  "brightnessDown\\circle\\brightnessDownCircle{:>03}.jpg"
    locations.outputBrightnessDownStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                         "brightnessDown\\star\\brightnessDownStar{:>03}.jpg"
    locations.outputBrightnessDownSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                           "brightnessDown\\square\\brightnessDownSquare{:>03}.jpg"

    # Flip
    locations.outputFlipVertical = ""
    locations.outputFlipHorizontal = ""
    locations.outputFlipElseVertical = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                               "flip\\else\\flipElseVertical{:>03}.jpg"
    locations.outputFlipElseHorizontal = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                             "flip\\else\\flipElseHorizontal{:>03}.jpg"
    locations.outputFlipCircleVertical = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                "flip\\circle\\flipCircleVertical{:>03}.jpg"
    locations.outputFlipCircleHorizontal = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                              "flip\\circle\\flipCircleHorizontal{:>03}.jpg"
    locations.outputFlipStarVertical = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                       "flip\\star\\flipStarVertical{:>03}.jpg"
    locations.outputFlipStarHorizontal = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                         "flip\\star\\flipStarHorizontal{:>03}.jpg"
    locations.outputFlipSquareVertical = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                         "flip\\square\\flipSquareVertical{:>03}.jpg"
    locations.outputFlipSquareHorizontal = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                           "flip\\Square\\flipSquareHorizontal{:>03}.jpg"

    # Contrast Up
    locations.outputContrastUp = ""
    locations.outputContrastUpElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                               "contrastUp\\else\\contrastUpElse{:>03}.jpg"
    locations.outputContrastUpCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                "contrastUp\\circle\\contrastUpCircle{:>03}.jpg"
    locations.outputContrastUpStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                     "contrastUp\\star\\contrastUpStar{:>03}.jpg"
    locations.outputContrastUpSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                       "contrastUp\\square\\contrastUpSquare{:>03}.jpg"

    # Contrast Down
    locations.outputContrastDown = ""
    locations.outputContrastDownElse = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                     "contrastDown\\else\\contrastDownElse{:>03}.jpg"
    locations.outputContrastDownCircle = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                       "contrastDown\\circle\\contrastDownCircle{:>03}.jpg"
    locations.outputContrastDownStar = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                     "contrastDown\\star\\contrastDownStar{:>03}.jpg"
    locations.outputContrastDownSquare = "C:\\Users\\rrb12\\Desktop\\image_manipulations\\" \
                                       "contrastDown\\square\\contrastDownSquare{:>03}.jpg"


# Function that processes the task selecting
def classifier():
    selector = input("0 - Else\n1 - Circle\n2 - Star\n3 - Squire\nYour choice: ")
    sel = int(selector)

    locations()
    if sel == 0:
        classifier.inputImageDir = locations.inputImageDirElse
        classifier.outputCleanUp = locations.outputCleanUpElse
        classifier.outputRotate = locations.outputRotateElse
        classifier.outputTranslation = locations.outputTranslationElse
        classifier.outputAffineTransformation = locations.outputAffineTransformationElse
        classifier.outputPerspectiveTransformation = locations.outputPerspectiveTransformationElse
        classifier.outputBrightnessUp = locations.outputBrightnessUpElse
        classifier.outputBrightnessDown = locations.outputBrightnessDownElse
        classifier.outputFlipVertical = locations.outputFlipElseVertical
        classifier.outputFlipHorizontal = locations.outputFlipElseHorizontal
        classifier.outputContrastUp = locations.outputContrastUpElse
        classifier.outputContrastDown = locations.outputContrastDownElse

    elif sel == 1:
        classifier.inputImageDir = locations.inputImageDirCircle
        classifier.outputCleanUp = locations.outputCleanUpCircle
        classifier.outputRotate = locations.outputRotateCircle
        classifier.outputTranslation = locations.outputTranslationCircle
        classifier.outputAffineTransformation = locations.outputAffineTransformationCircle
        classifier.outputPerspectiveTransformation = locations.outputPerspectiveTransformationCircle
        classifier.outputBrightnessUp = locations.outputBrightnessUpCircle
        classifier.outputBrightnessDown = locations.outputBrightnessDownCircle
        classifier.outputFlipVertical = locations.outputFlipCircleVertical
        classifier.outputFlipHorizontal = locations.outputFlipCircleHorizontal
        classifier.outputContrastUp = locations.outputContrastUpCircle
        classifier.outputContrastDown = locations.outputContrastDownCircle

    elif sel == 2:
        classifier.inputImageDir = locations.inputImageDirStar
        classifier.outputCleanUp = locations.outputCleanUpStar
        classifier.outputRotate = locations.outputRotateStar
        classifier.outputTranslation = locations.outputTranslationStar
        classifier.outputAffineTransformation = locations.outputAffineTransformationStar
        classifier.outputPerspectiveTransformation = locations.outputPerspectiveTransformationStar
        classifier.outputBrightnessUp = locations.outputBrightnessUpStar
        classifier.outputBrightnessDown = locations.outputBrightnessDownStar
        classifier.outputFlipVertical = locations.outputFlipStarVertical
        classifier.outputFlipHorizontal = locations.outputFlipStarHorizontal
        classifier.outputContrastUp = locations.outputContrastUpStar
        classifier.outputContrastDown = locations.outputContrastDownStar

    elif sel == 3:
        classifier.inputImageDir = locations.inputImageDirSquare
        classifier.outputCleanUp = locations.outputCleanUpSquare
        classifier.outputRotate = locations.outputRotateSquare
        classifier.outputTranslation = locations.outputTranslationSquare
        classifier.outputAffineTransformation = locations.outputAffineTransformationSquare
        classifier.outputPerspectiveTransformation = locations.outputPerspectiveTransformationSquare
        classifier.outputBrightnessUp = locations.outputBrightnessUpSquare
        classifier.outputBrightnessDown = locations.outputBrightnessDownSquare
        classifier.outputFlipVertical = locations.outputFlipSquareVertical
        classifier.outputFlipHorizontal = locations.outputFlipSquareHorizontal
        classifier.outputContrastUp = locations.outputContrastUpSquare
        classifier.outputContrastDown = locations.outputContrastDownSquare
    else:
        exit()


# F O L D E R   F O R   U N P R O C E S S E D   I M A G E S
image_path_list = []
valid_image_extensions = [".jpg", ".png"]
valid_image_extensions = [item.lower() for item in valid_image_extensions]

classifier()
for file in os.listdir(classifier.inputImageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(classifier.inputImageDir, file))


# M E N U
def menu():
    print("\n")
    print("-------I M A G E     M A N I P U L A T O R-------")
    print("--------------------M E N U----------------------")
    print("0 - Clean Up")
    print("2 - Rotate")
    print("3 - Translation")
    print("4 - Affine Translation")
    print("5 - Perspective Translation")
    print("6 - Brightness up")
    print("7 - Brightness down")
    print("8 - Flip")
    print("9 - Contrast Up")
    print("10 - Contrast Down")
    print("11 - Exit")


# 0 - C L E A N    U P
def cleanUp():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)
            # src, dst, h, hColor, templateWindowSize, searchWindowSize
            clean = cv2.fastNlMeansDenoisingColored(img, None, 20, 15, 17, 21)
            cv2.resize(clean, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
            cv2.imwrite(classifier.outputCleanUp.format(idx), clean)
            end = time.time()
            print(f"Saved {classifier.outputCleanUp.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 2 - R O T A T E
def rotate():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)
            rows, cols, ch = img.shape
            M = cv2.getRotationMatrix2D((cols/2, rows/2), random.randint(0, 360), 1)
            dst = cv2.warpAffine(img, M, (cols, rows))
            cv2.imwrite(classifier.outputRotate.format(idx), dst)
            end = time.time()
            print(f"Saved {classifier.outputRotate.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 3 - T R A N S L A T I O N
def translation():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)
            rows, cols, ch = img.shape
            M = np.float32([[1, 0, 100], [0, 1, 50]])
            dst = cv2.warpAffine(img, M, (cols, rows))
            crop_img = dst[50:365, 100:490]
            cv2.imwrite(classifier.outputTranslation.format(idx), crop_img)
            end = time.time()
            print(f"Saved {classifier.outputTranslation.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 4 - A F F I N E
def affineTransformation():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)
            rows, cols, ch = img.shape
            pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
            pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
            M = cv2.getAffineTransform(pts1, pts2)
            dst = cv2.warpAffine(img, M, (cols, rows))
            cv2.imwrite(classifier.outputAffineTransformation.format(idx), dst)
            end = time.time()
            print(f"Saved {classifier.outputAffineTransformation.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 5 - P E R S P E C T I V E
def perspectiveTransformation():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, image_path_list)
            img = cv2.imread(imagePath)
            pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
            pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
            M = cv2.getPerspectiveTransform(pts1, pts2)
            dst = cv2.warpPerspective(img, M, (300, 300))
            cv2.imwrite(classifier.outputPerspectiveTransformation.format(idx), dst)
            end = time.time()
            print(f"Saved {classifier.outputPerspectiveTransformation.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 6 - B R I G H T N E S S   U P
def brightnessUp():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)
            new_image = np.zeros(img.shape, img.dtype)

            alpha = random.uniform(1, 3)
            print(f"alpha: {alpha}")
            beta = random.uniform(0, 100)
            print(f"beta: {beta}")

            print("Please wait...")

            for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    for c in range(img.shape[2]):
                        new_image[y, x, c] = np.clip(alpha*img[y, x, c] + beta, 0, 255)
            cv2.imwrite(classifier.outputBrightnessUp.format(idx), new_image)
            end = time.time()
            print(f"Saved - {classifier.outputBrightnessUp.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 7 - B R I G H T N E S S   D O W N
def brightnessDown():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)
            new_image = np.zeros(img.shape, img.dtype)

            alpha = random.uniform(1, 3)
            print(f"alpha: {alpha}")
            beta = random.uniform(0, 100)
            print(f"beta: {beta}")

            print("Please wait...")

            for y in range(img.shape[0]):
                for x in range(img.shape[1]):
                    for c in range(img.shape[2]):
                        new_image[y, x, c] = np.clip(alpha * img[y, x, c] - beta, 0, 255)
            cv2.imwrite(classifier.outputBrightnessDown.format(idx), new_image)
            end = time.time()
            print(f"Saved - {classifier.outputBrightnessDown.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 8 - F L I P
def flip():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)
            horizontal_img = cv2.flip(img, 0)
            vertical_img = cv2.flip(img, 1)

            cv2.imwrite(classifier.outputFlipVertical.format(idx), vertical_img)
            print("Saved\n")

            cv2.imwrite(classifier.outputFlipHorizontal.format(idx), horizontal_img)
            end = time.time()
            print(f"Saved - {classifier.outputFlipHorizontal.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 9 - C O N T R A S T   U P
def contrastUp():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)

            # alpha=1  beta=0      --> no change
            # 0 < alpha < 1        --> lower contrast
            # alpha > 1            --> higher contrast
            # -127 < beta < +127   --> good range for brightness values
            alpha = random.uniform(1.1, 10)
            print(f"alpha: {alpha}")

            beta = random.uniform(0, 100)
            print(f"beta: {beta}")

            # image, alpha, image, beta, gamma
            output = cv2.addWeighted(img, alpha, img, beta, 0)

            cv2.imwrite(classifier.outputContrastUp.format(idx), output)
            end = time.time()
            print(f"Saved - {classifier.outputContrastUp.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


# 10 - C O N T R A S T   D O W N
def contrastDown():
    if len(os.listdir(classifier.inputImageDir)) == 0:
        print("Folder is empty\n")
    else:
        for idx, imagePath in enumerate(image_path_list):
            start = time.time()
            print(idx, imagePath)
            img = cv2.imread(imagePath)

            # alpha=1  beta=0      --> no change
            # 0 < alpha < 1        --> lower contrast
            # alpha > 1            --> higher contrast
            # -127 < beta < +127   --> good range for brightness values
            alpha = random.uniform(0.1, 0.9)
            print(f"alpha: {alpha}")

            beta = random.uniform(0, 100)
            print(f"beta: {beta}")

            # image, alpha, image, beta, gamma
            output = cv2.addWeighted(img, alpha, img, beta, 0)

            cv2.imwrite(classifier.outputContrastDown.format(idx), output)
            end = time.time()
            print(f"Saved - {classifier.outputContrastDown.format(idx)}\nelapsed time: {(end - start)} sec\n")
    main()


def main():
    menu()
    try:
        select = input("\nMake your choice = ")
        sel = int(select)

        if sel == 0:
            cleanUp()

        elif sel == 2:
            rotate()

        elif sel == 3:
            translation()

        elif sel == 4:
            affineTransformation()

        elif sel == 5:
            perspectiveTransformation()

        elif sel == 6:
            brightnessUp()

        elif sel == 7:
            brightnessDown()

        elif sel == 8:
            flip()

        elif sel == 9:
            contrastUp()

        elif sel == 10:
            contrastDown()

        elif sel == 11:
            exit()

        else:
            print("Great work, you couldn't press a single button from 0 to 11")
            menu()
    except ValueError:
        print("Error, not a number")


main()
