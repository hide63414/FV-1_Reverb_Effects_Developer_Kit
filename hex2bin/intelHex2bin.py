def hex_to_bin(hex_file, bin_file):
    with open(hex_file, 'r') as f_hex:
        lines = f_hex.readlines()
    
    data = []
    for line in lines:
        if line.startswith(':'):
            byte_count = int(line[1:3], 16)
            address = int(line[3:7], 16)
            record_type = int(line[7:9], 16)
            content = line[9:9 + byte_count * 2]
            
            if record_type == 0x00:  # Data record
                data.extend([content[i:i+2] for i in range(0, len(content), 2)])
    
    with open(bin_file, 'wb') as f_bin:
        f_bin.write(bytearray(int(byte, 16) for byte in data))

# 使用例
hex_to_bin('input.hex', 'output.bin')



