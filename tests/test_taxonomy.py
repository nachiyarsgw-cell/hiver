from src.model import weak_intent
def test_security(): assert weak_intent('Someone hacked my Amazon account')=='security_privacy'
def test_delivery(): assert weak_intent('Where is my package?')=='order_delivery'
