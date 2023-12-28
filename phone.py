import os, random, pygame
import subprocess
import time
import signal


pygame.mixer.init()

#Plays dialing tone
dialing = '/home/gauchos/Music/dialing.wav'
pygame.mixer.music.load(dialing)
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
	pass


#Select random message from Fuego Austral 
randomfile = random.choice(os.listdir("/home/gauchos/Music/msgfa"))
file = '/home/gauchos/Music/msgfa/'+ randomfile
print ("Calling Fuego Austral",randomfile,"...")

#Plays message
pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	pass


input("Press enter to record 60 seconds message")

#>Records Message
message_date = time.localtime()
message_date = time.strftime("%Y%m%d_%H%M%S", message_date)
message = '/home/gauchos/Music/msgbm/'+ message_date

proc_args = ['arecord', '-D' , 'plughw:2,0' , '-c1' , '-r' , '44100' , '-f' , 'S32_LE' , '-t' , 'wav' , '-V' , 'mono' , '-v' , message]
rec_proc = subprocess.Popen(proc_args, shell=False, preexec_fn=os.setsid)
print("startRecordingArecord()> rec_proc pid= " + str(rec_proc.pid))
print("startRecordingArecord()> recording started")

time.sleep(10)
os.killpg(rec_proc.pid, signal.SIGTERM)
rec_proc.terminate()
rec_proc = None
print("stopRecordingArecord()> Recording stopped")
