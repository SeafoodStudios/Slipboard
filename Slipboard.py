import rumps
import copykitten
import webbrowser
import subprocess

global data
data = []

class Slipboard(rumps.App):
    @rumps.clicked("Paste to Slip")
    def paste(self, sender):
        data.append(copykitten.paste())
    @rumps.clicked("Copy from Slip")
    def copy(self, sender):
        slipboard = "Slipboard"
        if not len(data) == 0:
            for i in range(len(data)):
                slipboard = slipboard + "\n━━━━━━━━━\n" + data[i]
            file_path = "/tmp/slipboard.txt"
            with open(file_path, "w") as f:
                f.write("\n━━━━━━━━━\n".join(data))
            subprocess.run(["open", file_path])
        else:
            rumps.alert("Your Slipboard is empty!")
    @rumps.clicked("Clear Slipboard")
    def clear(self, sender):
        global data
        data = []
        rumps.notification("Slipboard Cleared", "", "")
if __name__ == "__main__":
    Slipboard("Slipboard").run()
