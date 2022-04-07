# with open('test.txt', 'r') as f:
#     size_to_read = 10

    # f_contents = f.read(size_to_read)

    # while len(f_contents) > 0:
    #     print(f_contents, end='/')
    #     f_contents = f.read(size_to_read) # f_contents = remainders of the file

    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # f.seek(2)

    # f_contents = f.read(size_to_read)
    # print(f_contents)


# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('llama-corn.jpeg', 'rb') as rf:
#     with open('llama-corn-copy.jpeg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)


with open('llama-corn.jpeg', 'rb') as rf:
    with open('llama-corn-copy.jpeg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)