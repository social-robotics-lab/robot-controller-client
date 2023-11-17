import argparse
import time
from robottools import RobotTools


parse = argparse.ArgumentParser()
parse.add_argument('--ip', required=True)
parse.add_argument('--port', default=22222, type=int)
args = parse.parse_args()

print('テスト開始')
print('ロボットのIPアドレス:', args.ip)

rt = RobotTools(args.ip, args.port)
time.sleep(3)


print('現在の関節角度を取得する。')
axes = rt.read_axes()
print(axes)
time.sleep(3)


print('1秒間で左手を上げる。')
servo_map = dict(L_SHOU=0)
pose = dict(Msec=1000, ServoMap=servo_map)
rt.play_pose(pose)
time.sleep(3)


print('0.5秒間で左手を下ろし、右手を上げ、反時計回りに30度回転し、両目の色を青にする。')
servo_map = dict(L_SHOU=-90, R_SHOU=0, BODY_Y=30)
led_map = dict(R_EYE_R=0, R_EYE_G=0, R_EYE_B=255,
               L_EYE_R=0, L_EYE_G=0, L_EYE_B=255)
pose = dict(Msec=500, ServoMap=servo_map, LedMap=led_map)
rt.play_pose(pose)
time.sleep(3)
  

print('ポーズをリセットする。')
servo_map = dict(HEAD_R=0, HEAD_P=-5, HEAD_Y=0, BODY_Y=0, 
                 L_SHOU=-90, L_ELBO=0, R_SHOU=90, R_ELBO=0)
led_map = dict(L_EYE_R=255, L_EYE_G=255, L_EYE_B=255, 
               R_EYE_R=255, R_EYE_G=255, R_EYE_B=255)
pose = dict(Msec=1000, ServoMap=servo_map, LedMap=led_map)
rt.play_pose(pose)
time.sleep(3)


print('1秒間で左手を挙げる動作を0.3秒後に止める。')
servo_map = dict(L_SHOU=0)
pose = dict(Msec=1000, ServoMap=servo_map)
rt.play_pose(pose)
time.sleep(0.3)
rt.stop_pose()
time.sleep(3)
   

print('モーション（ポーズのリスト）を実行する。')
nod_motion = [
    dict(Msec=250, ServoMap=dict(R_SHOU=105,HEAD_P=-15,R_ELBO=0, L_ELBO=-3, L_SHOU=-102)),
    dict(Msec=250, ServoMap=dict(R_SHOU=77, HEAD_P=20, R_ELBO=17,L_ELBO=-17,L_SHOU=-79 )),
    dict(Msec=250, ServoMap=dict(R_SHOU=92, HEAD_P=-5, R_ELBO=5, L_ELBO=-7, L_SHOU=-88 ))
]
rt.play_motion(nod_motion)
time.sleep(3)


print('モーションを0.25秒後に止める。')
nod_motion = [
    dict(Msec=250, ServoMap=dict(R_SHOU=105,HEAD_P=-15,R_ELBO=0, L_ELBO=-3, L_SHOU=-102)),
    dict(Msec=250, ServoMap=dict(R_SHOU=77, HEAD_P=20, R_ELBO=17,L_ELBO=-17,L_SHOU=-79 )),
    dict(Msec=250, ServoMap=dict(R_SHOU=92, HEAD_P=-5, R_ELBO=5, L_ELBO=-7, L_SHOU=-88 ))
]
rt.play_motion(nod_motion)
time.sleep(0.25)
rt.stop_motion()
time.sleep(3)


print('アイドル動作を実行する（10秒）。')
rt.play_idle_motion()
time.sleep(10)


print('アイドル動作を止める。')
rt.stop_idle_motion()
time.sleep(3)
 

print('5秒のビートジェスチャを生成し実行する。')
beat_motion = rt.make_beat_motion(5.0)
d = rt.play_motion(beat_motion)
time.sleep(5.0)
time.sleep(3)


print('wavファイルを再生する。')
d = rt.play_wav('sample.wav')
time.sleep(d)
time.sleep(3)
 

print('Wavファイルの再生とビートジェスチャを組み合わせる。')
d = rt.play_wav('sample.wav')
beat_motion = rt.make_beat_motion(d)
rt.play_motion(beat_motion)
time.sleep(d)
time.sleep(3)


print('任意の言葉を発話する')
s = input('発話を入力してください：')
d = rt.say_text(s)
time.sleep(d)
time.sleep(3)


print('発話しながらビートジェスチャをする。')
s = input('少し長めの発話を入力してください：')
d = rt.say_text(s)
beat_motion = rt.make_beat_motion(d)
rt.play_motion(beat_motion)
time.sleep(d)
time.sleep(3)


print('以上でテストは終了です。')
