import rpyc


class RPyCServer(rpyc.Service):
    ROOT_FOLDER = "files\\"

    def exposed_get_file(self, file_name):
        """
        Let the client get the content of a file
        :param file_name: the file's name
        :return: the content of the wanted file
        """
        try:
            with open(self.ROOT_FOLDER+file_name, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            return "The file was not found"
        return file_content

    def exposed_put_file(self, file_name, file_content):
        """
        Let the client put a string in a file on the server
        :param file_name: the file's name
        :param file_content: the file's content
        """
        with open(self.ROOT_FOLDER+file_name, "w") as file:
            file.write(file_content)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RPyCServer, port=25565)
    t.start()