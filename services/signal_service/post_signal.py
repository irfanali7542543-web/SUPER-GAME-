import time

def post_signal():
    print("FX Master Signal System Started...")
    while True:
        # Yahan aapka signal logic aayega
        print("Signal: BUY EURUSD at 1.0850")
        time.sleep(10) # Har 10 second baad signal dikhayega

if __name__ == "__main__":
    post_signal()

