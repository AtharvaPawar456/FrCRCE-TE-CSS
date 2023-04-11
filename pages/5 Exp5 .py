# import hashlib
# import streamlit as st

# st.header("CSS Exp - 5 MD5 & SHA1")



# # hexadecimal (MD5 and SHA-1)
# msgarray = ["1234567890", "abcdefghijklm\nnopqrstuvwxyz", "message digest"]
# md5_result = []
# sha1_result = []

# # for MD5
# for item in msgarray:
#     result = hashlib.md5(item.encode())
#     md5_result.append(result.hexdigest())

# # for SHA1
# for item in msgarray:
#     result = hashlib.sha1(item.encode())
#     sha1_result.append(result.hexdigest())

# for i in range(len(msgarray)):
#     print(
#         f'Message{i+1}:{msgarray[i]} \t\t  MD5: {md5_result[i]}  \t SHA-1 : {sha1_result[i]}')
    



import hashlib
import streamlit as st

def Simple():
    st.header("CSS Exp - 5 MD5 & SHA1")

    msgarray = []
    msg_count = st.number_input("Enter the number of messages", min_value=1, step=1)

    # take input messages from the user
    for i in range(msg_count):
        msg = st.text_input(f"Enter message {i+1}",value="Note that in practice, you should handle errors and exceptions properly")
        msgarray.append(msg)

    md5_result = []
    sha1_result = []

    # for MD5
    for item in msgarray:
        result = hashlib.md5(item.encode())
        md5_result.append(result.hexdigest())

    # for SHA1
    for item in msgarray:
        result = hashlib.sha1(item.encode())
        sha1_result.append(result.hexdigest())

    # display the results
    for i in range(len(msgarray)):
        st.info(f"Message{i+1}:{msgarray[i]}")
        st.warning(f"MD5: {md5_result[i]}")
        st.warning(f"SHA-1: {sha1_result[i]}")


    text = st.text_area("Enter some text here")

    # display the input
    st.write("You entered:")
    st.write(text)











# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import timeit
import hashlib
def TimeCompare():
    msgarray = ["1234567890", "abcdefghijklm\nnopqrstuvwxyz", "message digest"]
    md5_result = []
    sha1_result = []

    # for MD5
    def MD5(data):
        result = hashlib.md5(data.encode())
        md5_result.append(result.hexdigest())

    # for SHA1
    def sha1(data):
        result = hashlib.sha1(data.encode())
        sha1_result.append(result.hexdigest())


    def main(fileitem, tog):

        if tog == 0:
            MD5(fileitem)
        else:
            sha1(fileitem)

    # def main(fileitem, tog):
    #     text_file = open(fileitem, "r")
    #     data = text_file.read()
    #     if tog == 0:
    #         MD5(data)
    #     else:
    #         sha1(data)

    #     text_file.close()

    tstartmd5 = []
    tendmd5 = []
    tstartsha = []
    tendsha = []

    _1Kuploaded_file = st.file_uploader("Choose a 1k size of text file", type="txt", key="file1")
    _5Kuploaded_file = st.file_uploader("Choose a 5k size of text file", type="txt", key="file2")
    _10Kuploaded_file = st.file_uploader("Choose a 10k size of text file", type="txt", key="file3")

    # Check if a file was uploaded
    if _1Kuploaded_file is not None:
        # Read the contents of the file
        file_contents = _1Kuploaded_file.read()

        # Decode the contents as UTF-8 text
        _1kfile_text = file_contents.decode("utf-8")

        if st.button("View Content of _1Kuploaded_file",key="con1"):
            # Display the text in the app
            st.write("File contents of _1Kuploaded_file:")
            st.write(_1kfile_text)

    # Check if a file was uploaded
    if _5Kuploaded_file is not None:
        # Read the contents of the file
        file_contents = _5Kuploaded_file.read()

        # Decode the contents as UTF-8 text
        _5kfile_text = file_contents.decode("utf-8")

        if st.button("View Content of _5Kuploaded_file",key="con2"):
            # Display the text in the app
            st.write("File contents of _5Kuploaded_file:")
            st.write(_5kfile_text)

    # Check if a file was uploaded
    if _10Kuploaded_file is not None:
        # Read the contents of the file
        file_contents = _10Kuploaded_file.read()

        # Decode the contents as UTF-8 text
        _10kfile_text = file_contents.decode("utf-8")

        if st.button("View Content of _10Kuploaded_file",key="con3"):
            # Display the text in the app
            st.write("File contents of _10Kuploaded_file:")
            st.write(_10kfile_text)

    if _1Kuploaded_file is not None and _5Kuploaded_file is not None and _10Kuploaded_file is not None:
        filePath = [_1kfile_text, _5kfile_text, _10kfile_text]
        filePathName = ["_1kfile_text", "_5kfile_text", "_10kfile_text"]
        results = []

        for i in range(len(filePath)):
            tstartmd5.append(timeit.default_timer())
            main(filePath[i], 0, )
            tendmd5.append(timeit.default_timer())
            elapsed_time_md5 = round((tendmd5[i] - tstartmd5[i]) * 10 ** 6, 3)

            tstartsha.append(timeit.default_timer())
            main(filePath[i], 1)
            tendsha.append(timeit.default_timer())
            elapsed_time_sha1 = round((tendsha[i] - tstartsha[i]) * 10 ** 6, 3)

            results.append({'File': filePathName[i], 'MD5 (µs)': elapsed_time_md5, 'SHA-1 (µs)': elapsed_time_sha1})

        st.table(results)


if __name__ == "__main__":
    st.markdown('''<h1 style="color: aquamarine;">Hashing with Salt and Pepper</h1>''', unsafe_allow_html=True)
    st.markdown("""<br>""",unsafe_allow_html=True)


    options = ['Simple','TimeCompare' ]
    selected_option = st.selectbox(' ', options)

    # st.write('You selected:', selected_option)

    if selected_option == "Simple":
        Simple()

    if selected_option == "TimeCompare":
        TimeCompare()





# '''
# OUTPUT:

# Elapsed time for txt-data\_1K.txt:      for MD5         : 277.3 µs
# Elapsed time for txt-data\_5K.txt:      for MD5         : 302.7 µs
# Elapsed time for txt-data\_10K.txt:     for MD5         : 363.7 µs
# ------------------------------------------------------
# Elapsed time for txt-data\_1K.txt:      for SHA-1       : 389.3 µs
# Elapsed time for txt-data\_5K.txt:      for SHA-1       : 372.6 µs
# Elapsed time for txt-data\_10K.txt:     for SHA-1       : 351.0 µs

# '''




# '''
# Output:
# Message1:1234567890                     MD5: e807f1fcf82d132f9bb018ca6738a19f          SHA-1 : 01b307acba4f54f55aafc33bb06bbbf6ca803e9a
# Message2:abcdefghijklmnopqrstuvwxyz     MD5: d74374c383e44213e4f17a0fe32a9a76          SHA-1 : 42f882085ab0a3dab86803118c6c00ed871553f0
# Message3:message digest                 MD5: f96b697d7cb7938d525a2f31aaf161d0          SHA-1 : c12252ceda8be8994d5fa0290a47231c1d16aae3
# '''
