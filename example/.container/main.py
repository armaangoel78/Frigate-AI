from frigate.wrapper import frigate_model

@frigate_model("input.jpg", "input.jpg")
def main():
    print("Model evaluation!")

if __name__ == '__main__':
    main("s3://frigate-ship/mark.jpg")
