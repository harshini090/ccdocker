import socket
import re
from collections import Counter

def main():
    file1 = "IF-1.txt"
    file2 = "AlwaysRememberUsThisWay-1.txt"
    with open(file1, "r", encoding="utf-8") as f:
        text1 = f.read()
    with open(file2, "r", encoding="utf-8") as f:
        text2 = f.read()
    words_file1 = text1.split()
    words_file2 = text2.split()
    count_file1 = len(words_file1)
    count_file2 = len(words_file2)
    total_count = count_file1 + count_file2
    cleaned_text1 = re.findall(r"[a-zA-Z']+", text1.lower())
    freq_file1 = Counter(cleaned_text1)
    top_3_file1 = freq_file1.most_common(3)
    cleaned_text2 = re.findall(r"[a-zA-Z']+", text2.lower())
    expanded_words = []
    for w in cleaned_text2:
        expanded_words.extend(w.split("'"))
    expanded_words = [w for w in expanded_words if w != '']
    freq_file2 = Counter(expanded_words)
    top_3_file2 = freq_file2.most_common(3)
    container_ip = socket.gethostbyname(socket.gethostname())
    results = []
    results.append(f"Words in IF-1.txt: {count_file1}")
    results.append(f"Words in AlwaysRememberUsThisWay-1.txt: {count_file2}")
    results.append(f"Total words (both files): {total_count}")
    results.append("Top 3 most frequent words in IF-1.txt:")
    for word, cnt in top_3_file1:
        results.append(f"{word}: {cnt}")
    results.append("Top 3 most frequent words in AlwaysRememberUsThisWay-1.txt (with contractions split):")
    for word, cnt in top_3_file2:
        results.append(f"{word}: {cnt}")
    results.append(f"Container IP: {container_ip}")
    with open("output/result.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(results))
    print("\n".join(results))

if __name__ == "__main__":
    main()

