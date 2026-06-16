from seal import tokenizer

# Example 1: Normal input
user_input = "The cat sat on the mat. The cat was happy!"
result = tokenizer(user_input)

if result["error"]:
    print(f"❌ Error: {result['error']}")
else:
    print(f"✅ Tokens: {result['tokens']}")
    print(f"📊 Total Length: {result['length']}")
    print(f"🔑 Key-Value (Frequencies): {result['frequencies']}")

print("\n" + "-" * 40 + "\n")

# Example 2: Empty input 
empty_text = ""
result2 = tokenizer(empty_text)
print(f"❌ Error: {result2['error']}")  

print("\n" + "-" * 40 + "\n")

# Example 3: Non-string input 
bad_input = 12345
result3 = tokenizer(bad_input)
print(f"❌ Error: {result3['error']}")