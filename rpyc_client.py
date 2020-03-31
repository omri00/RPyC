import rpyc
PORT = 25565
HOST = "localhost"


def write_in_server(client, file_name):
    """
    Ask for the content of the file and write it in the server
    :param client: the client
    :param file_name: the file's name
    """
    content = input("Enter the content you want the file to have\n")
    client.root.put_file(file_name, content)


if __name__ == '__main__':
    client = rpyc.connect(HOST, PORT)
    file_name = input("Enter the name of the file you want in the server\n")
    write_in_server(client, file_name)
    print(client.root.get_file(file_name))
