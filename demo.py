import serial
import time

# 7x28のドットマトリクスを定義
#mokutti
matrix = [
    "0000000000000000000000000000",
    "0000000000100000000000000010",
    "1101100000100000000100010000",
    "1010101110101010101110111010",
    "1010101010110010100100010010",
    "1000101110101011100110011010",
    "0000000000000000000000000000"
]

# 7x28のドットマトリクスを定義
#matrix = [
#    "0000000000000000000000000000",
#    "0000000000000000000000000000",
#    "0000000000000000000000000000",
#    "0000000000000000000000000000",
#    "0000000000000000000000000000",
#    "0000000000000000000000000000",
#    "0000000000000000000000000000"
#]

# 7x28のマトリクスをflipdotディスプレイに送信する関数
def send_to_flipdot(matrix):
    data_bytes = bytearray()
    for col in range(28):
        col_data = 0
        for row in range(7):
            if matrix[row][col] == '1':
                col_data |= (1 << row)
        data_bytes.append(col_data)

    transmission = bytearray([0x80, 0x83, 0xFF]) + data_bytes + bytearray([0x8F])

    with serial.Serial("/dev/serial0", 9600) as srl:
        srl.write(transmission)

# 初めに全てのドットを消灯するデータ
all_dark = bytearray([
    0x80,  # ヘッダー
    0x83,  # 28バイト、リフレッシュ
    0xFF,  # アドレス
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # 28バイトのデータ
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x8F # EOT
])

# シリアルポートを開き、全てのドットを消灯
with serial.Serial("/dev/serial0", 9600) as srl:
    srl.write(all_dark)
    time.sleep(1)
    # パターンを送信
    send_to_flipdot(matrix)
