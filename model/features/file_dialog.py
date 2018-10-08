import webview

class Feature():

    def __init__(self):
        pass

    @classmethod
    def data(cls):
        return "Nothing yet!"

    @classmethod
    def action(cls):
        file_path = webview.create_file_dialog()
        return file_path

if __name__ == "__main__":
    pass