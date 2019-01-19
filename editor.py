import cv2


def play_video(video_name):
    cap = cv2.VideoCapture(video_name)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('frame', frame)
            ch = 0xFF & cv2.waitKey(25)
            if ch == 27:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def cut_video(inpu, output, time_len, num_def=1):
    videoCapture = cv2.VideoCapture(inpu)

    videorate = videoCapture.get(cv2.CAP_PROP_FPS)
    allcnt = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

    for i in range(num_def):
        video_writer = cv2.VideoWriter('cutVideo.mp4',
                                       cv2.VideoWriter_fourcc(*'XVID'),
                                       videorate,
                                       (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        cnt = time_len * videorate

        startfra = int(allcnt / (num_def + 1) * (i + 1) - cnt / 2)

        if startfra < 0:
            startfra = 0
        elif startfra >= allcnt:
            startfra = allcnt - 1

        videoCapture.set(cv2.CAP_PROP_POS_FRAMES, startfra)
        success, frame = videoCapture.read()

        while success and cnt > 0:
            video_writer.write(frame)
            success, frame = videoCapture.read()
            cnt -= 1
    videoCapture.release()
    cv2.destroyAllWindows()


def change_speed(video_name, output, times):
    cap = cv2.VideoCapture(video_name)
    ret, frame = cap.read()
    height = frame.shape[0]
    width = frame.shape[1]
    fps = int(cap.get(cv2.CAP_PROP_FPS)*times)
    out = cv2.VideoWriter('changedSpeedVideo.mp4', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height), 1)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    out.release()


def join(videofiles):
    video_index = 0
    cap = cv2.VideoCapture(videofiles[0])
    ret, frame = cap.read()
    height = frame.shape[0]
    width = frame.shape[1]
    out = cv2.VideoWriter("joinedVideos.mp4", cv2.VideoWriter_fourcc(*'XVID'), 20.0, (width, height), 1)
    while True:
        ret, frame = cap.read()
        if frame is None:
            video_index += 1
            if video_index >= len(videofiles):
                break
            cap = cv2.VideoCapture(videofiles[video_index])
            ret, frame = cap.read()
        out.write(frame)
    cap.release()
    out.release()
    cv2.destroyAllWindows()

