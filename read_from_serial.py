from parnav_pb2 import BTIQSampleType, IqSample, IqSample16, BTIQSamplesReport
import serial

def main():
    # TODO: Not correct baudrade
    with serial.Serial('/dev/ttyS0', baudrate=115200) as ser:
        data = ser.readline()
        report = IqSample()
        try:
            report.ParseFromString(data)
            print(f"I: {report.i} Q: {report.q}")
        except:
            pass

if __name__ == "__main__":
    main()
