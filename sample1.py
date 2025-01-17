if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and
if ar_file is not None and

ar_file = st.file_uploader("Upload Excel or CSV file of Account Receivables", type=["xlsx", "xls", "csv"])
ap_file = st.file_uploader("Upload Excel or CSV file of Account Payables", type=["xlsx", "xls", "csv"])

file = st.file_uploader("Upload Excel or CSV file", type=["xlsx", "xls", "csv"])

if st.button("Submit"):
    if file is not None:
        message = churn_train_fn(file)
        st.write("Model Train Status: ", message) 

if st.button(key="churns-train", label="Train Model"):
    churn_train_dialog()