import serial
import time
import glob
import os

# シリアルポートの設定
ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

# コンソールにマトリクスを表示する関数
def print_matrix(matrix):
    for row in matrix:
        print(''.join(['■' if col == '1' else '□' for col in row]))
    print()

# データをflipdotディスプレイに送信する関数
def send_to_flipdot(matrix):
    data_bytes = bytearray()
    for col in range(28):
        col_data = 0
        for row in range(7):
            if matrix[row][col] == '1':
                col_data |= (1 << row)
        data_bytes.append(col_data)

    transmission = bytearray([0x80, 0x83, 0xFF]) + data_bytes + bytearray([0x8F])
    ser.write(transmission)

# フレームの保存先ディレクトリ
frame_files = sorted(glob.glob(os.path.join('frames', 'frame_*.txt')))
previous_frame = None

# フレームファイルを読み込み、表示および送信
for frame_file in frame_files:
    with open(frame_file, 'r') as file:
        matrix = [line.strip() for line in file.readlines()]

        # 前のフレームの0と1の部分を維持
        if previous_frame:
            for row in range(7):
                for col in range(28):
                    if previous_frame[row][col] == '0' and matrix[row][col] == '1':
                        matrix[row] = matrix[row][:col] + '1' + matrix[row][col + 1:]
                    elif previous_frame[row][col] == '1' and matrix[row][col] == '0':
                        matrix[row] = matrix[row][:col] + '0' + matrix[row][col + 1:]

        print_matrix(matrix)  # コンソールに表示
        send_to_flipdot(matrix)  # flipdotディスプレイに送信
        previous_frame = matrix
        time.sleep(1 / 15.27)  # フレームは15fpsだけどシリアル通信などで遅れるからそれも込みで15.27フレームレート

ser.close()