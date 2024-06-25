# Poker-Hand-Identifier-using-YOLO-and-OpenCV

This project is a Poker Hand Identifier that uses computer vision techniques to recognize and classify poker hands in real-time. By leveraging the power of OpenCV and a YOLO (You Only Look Once) model, this system can accurately detect playing cards and determine the poker hand they form.

## Key Features:
  1. **Real-Time Card Detection**: Utilizes a specialized poker card detector model, trained by me with YOLOv8 using [this dataset](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d/dataset/3) to detect and classify individual playing cards in a live video feed.
  2. **Hand Recognition**: Combines the detected cards to identify the specific poker hand (e.g., Full House, Straight, Flush).

## Repository Structure
  1. **main.py**: The main script that processes the video feed, detects cards using the YOLO model, and determines the poker hand. It integrates the detection and classification components to output the results in real time.
  2. **pokerFunction.py**: Contains helper functions for identifying poker hands based on detected cards.

![images (1)](https://github.com/MininduLiyanage/Poker-Hand-Identifier-using-YOLO-and-OpenCV/assets/73852035/e3b3e244-ea68-4b49-8afb-4510678f9a40)
