from abc import ABC, abstractmethod


# Command 인터페이스를 정의합니다.
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# 실제 작업을 수행하는 Receiver 클래스를 정의합니다.
class Light:
    def turn_on(self):
        print("전등을 켭니다.")

    def turn_off(self):
        print("전등을 끕니다.")


# Command 인터페이스를 구현하는 ConcreteCommand 클래스를 정의합니다.
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Invoker 클래스를 정의합니다.
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


if __name__ == "__main__":
    # Receiver 객체를 생성합니다.
    living_room_light = Light()

    # ConcreteCommand 객체를 생성합니다.
    turn_on_command = TurnOnLightCommand(living_room_light)
    turn_off_command = TurnOffLightCommand(living_room_light)

    # Invoker 객체를 생성하고 Command 객체를 설정합니다.
    remote = RemoteControl()
    remote.set_command(turn_on_command)

    # 버튼을 눌러서 작업을 실행합니다.
    remote.press_button()

    # 다른 Command 객체로 설정하고 다시 버튼을 눌러서 다른 작업을 실행합니다.
    remote.set_command(turn_off_command)
    remote.press_button()


"""
1. Command 인터페이스:
모든 ConcreteCommand 클래스가 구현해야 하는 execute 메서드를 선언하는 추상 클래스입니다.

2. Light 클래스:
실제 작업을 수행하는 Receiver 클래스로, 여기서는 전등을 켜고 끄는 작업을 수행합니다.

3. TurnOnLightCommand와 TurnOffLightCommand 클래스:
Command 인터페이스를 구현한 ConcreteCommand 클래스로, 각각 전등을 켜는 작업과 끄는 작업을 캡슐화합니다.

4. RemoteControl 클래스:
Invoker 역할을 하는 클래스로, Command 객체를 설정하고 버튼을 누르면 해당 Command를 실행합니다.

메인 부분에서는 실제 객체들을 생성하고 조합한 후, Invoker를 통해 Command를 실행하는 예시를 제공합니다.

커맨드 패턴은 작업의 실행을 캡슐화하고, 실행 취소 및 재실행과 같은 추가 기능을 구현하기에 용이하며,
요청과 실행 사이의 결합도를 낮추어 유지 보수와 확장성을 향상시키는 데 도움이 됩니다.
"""
