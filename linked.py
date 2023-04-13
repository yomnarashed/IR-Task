import os
import docx2txt

directory = "C:/Users/Yomna/OneDrive/Desktop/year3_term2/IR/section/"

search_word = input("Enter a word: ") 

# Build the inverted index
index = {}
for filename in os.listdir(directory):  # Loop over each file in the directory
    if filename.endswith(".doc") or filename.endswith(".docx"):  # Check  extension
        doc_text = docx2txt.process(os.path.join(directory, filename))  # Convert the Word file to text
        words = doc_text.split()  # Split the text into words
        doc_id = os.path.splitext(filename)[0]  # filename as the document ID
        for word in words:  # Loop over each word in the document
            if word not in index:  # If the word is not in the index, add it and its document ID
                index[word] = [doc_id]
            elif doc_id not in index[word]:  # If the word is in the index but the document ID is not, add the document ID
                index[word].append(doc_id)

postings_list = index.get(search_word, [])  # Get the postings list for the given word, or an empty list if the word is not in the index
if postings_list:  # If the postings list is not empty, print the document IDs
    print("Postings list:", ", ".join(str(doc_id) for doc_id in postings_list))
else:  # If the postings list is empty
    print("No documents contain the word", search_word)