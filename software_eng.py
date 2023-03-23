def encoder(data):
    data = ''
    for i in data:
        i = data + 3
    return data


# Jose Nodarse did the decoder
def decoder(data):
    final_data = ''
    encoded_data = 0
    runs = len(data)
    for i in range(runs):
        num = int(data[i])
        encoded_data += num - 3
        data += str(encoded_data)
        encoded_data = 0
    return final_data