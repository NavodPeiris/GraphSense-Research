






import numpy as np



def text_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding="utf-8", errors="surrogatepass"):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"



def emitter_converter(size_par, data):
    if size_par + len(data) <= 2**size_par - (len(data) - 1):
        raise ValueError("size of parity don't match with size of data")

    data_out = []
    parity = []
    bin_pos = [bin(x)[2:] for x in range(1, size_par + len(data) + 1)]

    
    data_ord = []
    
    data_out_gab = []
    
    qtd_bp = 0
    
    cont_data = 0

    for x in range(1, size_par + len(data) + 1):
        
        
        if qtd_bp < size_par:
            if (np.log(x) / np.log(2)).is_integer():
                data_out_gab.append("P")
                qtd_bp = qtd_bp + 1
            else:
                data_out_gab.append("D")
        else:
            data_out_gab.append("D")

        
        if data_out_gab[-1] == "D":
            data_ord.append(data[cont_data])
            cont_data += 1
        else:
            data_ord.append(None)

    
    qtd_bp = 0  
    for bp in range(1, size_par + 1):
        
        cont_bo = 0
        
        for cont_loop, x in enumerate(data_ord):
            if x is not None:
                try:
                    aux = (bin_pos[cont_loop])[-1 * (bp)]
                except IndexError:
                    aux = "0"
                if aux == "1" and x == "1":
                    cont_bo += 1
        parity.append(cont_bo % 2)

        qtd_bp += 1

    
    cont_bp = 0  
    for x in range(size_par + len(data)):
        if data_ord[x] is None:
            data_out.append(str(parity[cont_bp]))
            cont_bp += 1
        else:
            data_out.append(data_ord[x])

    return data_out


def receptor_converter(size_par, data):
    
    data_out_gab = []
    
    qtd_bp = 0
    
    cont_data = 0
    
    parity_received = []
    data_output = []

    for i, item in enumerate(data, 1):
        
        
        if qtd_bp < size_par and (np.log(i) / np.log(2)).is_integer():
            data_out_gab.append("P")
            qtd_bp = qtd_bp + 1
        else:
            data_out_gab.append("D")

        
        if data_out_gab[-1] == "D":
            data_output.append(item)
        else:
            parity_received.append(item)

    
    data_out = []
    parity = []
    bin_pos = [bin(x)[2:] for x in range(1, size_par + len(data_output) + 1)]

    
    data_ord = []
    
    data_out_gab = []
    
    qtd_bp = 0
    
    cont_data = 0

    for x in range(1, size_par + len(data_output) + 1):
        
        
        if qtd_bp < size_par and (np.log(x) / np.log(2)).is_integer():
            data_out_gab.append("P")
            qtd_bp = qtd_bp + 1
        else:
            data_out_gab.append("D")

        
        if data_out_gab[-1] == "D":
            data_ord.append(data_output[cont_data])
            cont_data += 1
        else:
            data_ord.append(None)

    
    qtd_bp = 0  
    for bp in range(1, size_par + 1):
        
        cont_bo = 0
        for cont_loop, x in enumerate(data_ord):
            if x is not None:
                try:
                    aux = (bin_pos[cont_loop])[-1 * (bp)]
                except IndexError:
                    aux = "0"
                if aux == "1" and x == "1":
                    cont_bo += 1
        parity.append(str(cont_bo % 2))

        qtd_bp += 1

    
    cont_bp = 0  
    for x in range(size_par + len(data_output)):
        if data_ord[x] is None:
            data_out.append(str(parity[cont_bp]))
            cont_bp += 1
        else:
            data_out.append(data_ord[x])

    ack = parity_received == parity
    return data_output, ack
