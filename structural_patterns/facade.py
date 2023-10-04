# 복잡한 오디오 재생 서브시스템 클래스들
class AudioPlayer:
    def play(self, file):
        print(f"Playing audio: {file}")


class VolumeControl:
    def set_volume(self, volume):
        print(f"Setting volume to {volume}")


# 퍼사드 클래스
class AudioSystemFacade:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.volume_control = VolumeControl()

    def play_audio(self, file):
        self.audio_player.play(file)

    def set_volume(self, volume):
        self.volume_control.set_volume(volume)


# 클라이언트 코드
if __name__ == "__main__":
    audio_system = AudioSystemFacade()

    # 오디오 재생 및 볼륨 조절
    audio_system.play_audio("song.mp3")
    audio_system.set_volume(50)
