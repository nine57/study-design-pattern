class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)


class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Handler A is handling the request")
        else:
            super().handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Handler B is handling the request")
        else:
            super().handle_request(request)


class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == "C":
            print("Handler C is handling the request")
        else:
            super().handle_request(request)


if __name__ == "__main__":
    handler_c = ConcreteHandlerC()
    handler_b = ConcreteHandlerB(handler_c)
    handler_a = ConcreteHandlerA(handler_b)

    handler_a.handle_request("A")
    handler_a.handle_request("B")
    handler_a.handle_request("C")
    handler_a.handle_request("D")


"""
1. Handler:
이 클래스는 요청을 처리할 수 있는 객체들의 기본 클래스입니다.
successor라는 속성을 가지며 다음 처리자를 가리킵니다.
handle_request 메서드를 정의하여 요청을 처리하거나 다음 처리자에게 전달합니다.

2. ConcreteHandlerA, ConcreteHandlerB, ConcreteHandlerC:
실제 요청을 처리할 구체적인 핸들러 클래스들입니다.
각 핸들러는 요청을 처리할 수 있는 조건을 검사하고 요청을 처리하거나 다음 처리자에게 전달합니다.
만약 처리 조건이 맞지 않으면 super().handle_request(request)를 호출하여 다음 처리자에게 요청을 전달합니다.

메인 부분에서는 핸들러 객체를 생성하고 연결한 후, 각 핸들러에게 다양한 요청을 보내고 그 결과를 출력합니다.

이렇게 구현된 책임 연쇄 패턴은 요청을 처리할 수 있는 핸들러를 동적으로 추가하거나 변경할 수 있으며,
객체 간의 결합도를 낮추는데 도움이 됩니다.
요청이 핸들러 체인을 따라 전파되어 적절한 핸들러에서 처리되게 됩니다.
"""
