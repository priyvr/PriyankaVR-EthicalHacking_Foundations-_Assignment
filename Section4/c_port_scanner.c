#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

void scan_port(int port) {
    int sock;
    struct sockaddr_in server;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons(port);

    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        printf("Port %d: CLOSED\n", port);
    } else {
        printf("Port %d: OPEN\n", port);
    }

    close(sock);
}

int main() {
    int ports[] = {22, 80, 443, 3306};

    for (int i = 0; i < 4; i++) {
        scan_port(ports[i]);
    }

    return 0;
}