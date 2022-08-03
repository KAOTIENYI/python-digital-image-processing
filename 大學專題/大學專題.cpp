
#include <opencv2/opencv.hpp>
#include <opencv2/dnn.hpp>
#include <iostream>
#include <string>
using namespace cv::dnn;
using namespace cv;
using namespace std;
int main(int argc, char** argv)
{   
	const int inWidth = 640;
	const int inHeight = 480;
	cout << "Run" << endl;
	Net net = readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel");

	setUseOptimized(1);
	VideoCapture cap(1);
	//VideoCapture cap("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3820, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink",CAP_GSTREAMER);
	cap.set(CAP_PROP_FRAME_WIDTH, inWidth);
	cap.set(CAP_PROP_FRAME_HEIGHT, inHeight);
	cap.set(CAP_PROP_AUTOFOCUS, 1);
	string window_name = "Display" + to_string(inWidth) + "x" + to_string(inHeight);
	namedWindow(window_name);
	while (getWindowProperty(window_name, WND_PROP_AUTOSIZE) >= 0)
	{
		Mat color_mat;
		cap >> color_mat;
		Mat inputBlob = blobFromImage(color_mat, 1.0, color_mat.size(), Scalar(104.0, 177.0, 123.0), false);
		net.setInput(inputBlob, "data");
		Mat detection = net.forward();

		Mat detectionMat(detection.size[2], detection.size[3], CV_32F, (float*)detection.data);
		
		float confidenceThreshold = 0.5;
		Vec3b color[] = { Vec3b(255,255,0),Vec3b(0,255,0), Vec3b(0,255,255), Vec3b(255,255,127) };
		int num = 0;
		for (int i = 0; i < detectionMat.rows; i++)
		{
			putText(color_mat, "Max size of Detections: " + to_string(detection.size[2]),
				Size(30, 30), FONT_HERSHEY_DUPLEX, 1, Scalar(0, 0, 255));
			float confidence = detectionMat.at<float>(i, 2);
			if (confidence > confidenceThreshold)
			{

				int x0 = (int)(detectionMat.at<float>(i, 3) * color_mat.cols);
				int y0 = (int)(detectionMat.at<float>(i, 4) * color_mat.rows);
				int x1 = (int)(detectionMat.at<float>(i, 5) * color_mat.cols);
				int y1 = (int)(detectionMat.at<float>(i, 6) * color_mat.rows);
				Rect object(x0, y0, x1 - x0 + 1, y1 - y0 + 1);
				cout << object;
				string ss = "#" + to_string(num++) + " Prob=" + to_string(confidence);
				cout << ss;

				if ((x0 + (x1 - x0 + 1) / 2) < inWidth / 2)
				{
					cout << "   L   ";
					cout << x0 + (x1 - x0 + 1) / 2 << endl;

				}
				else
				{
					cout << "   R   ";
					cout << x0 + (x1 - x0 + 1) / 2 << endl;
				}


				rectangle(color_mat, object, color[num % 4], 2);
				int baseLine = 0;
			
			}
		}
		imshow(window_name, color_mat);
		if (waitKey(100) == 27)break;
	}
	destroyAllWindows();
	return 0;
}
