from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
# model_name = "microsoft/DialoGPT-large"
model_name = "microsoft/DialoGPT-medium"
# model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

for step in range(5):
    # take user input
    text = input(">> You:")
    # encode the input and add end of string token
    input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
    # concatenate new user input with chat history (if there is)
    bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if step > 0 else input_ids

    # generate a bot response
    chat_history_ids = model.generate(
        # #case 1
        bot_input_ids,
        max_length=1000,
        #pad_token_id=tokenizer.eos_token_id,

        # case 2
        # num_beams=3,
        # early_stopping=True,
        # pad_token_id=tokenizer.eos_token_id

        #case 3
        # do_sample = True,
        # top_k=0,
        # pad_token_id=tokenizer.eos_token_id,

        # case 4
        # do_sample = True,
        # top_k=100,
        # temperature=0.75,
        # pad_token_id=tokenizer.eos_token_id,

        # case 5
        do_sample = True,
        top_p=0.95,
        top_k=0,
        temperature=0.75,
        pad_token_id=tokenizer.eos_token_id
    )

# chatting 5 times with nucleus & top-k sampling & tweaking temperature & multiple
# sentences

# # multiple choice
# for step in range(5):
#     # take user input
#     text = input(">> You:")
#     # encode the input and add end of string token
#     input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
#     # concatenate new user input with chat history (if there is)
#     bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) if step > 0 else input_ids
#     # generate a bot response
#     chat_history_ids_list = model.generate(
#         bot_input_ids,
#         max_length=1000,
#         do_sample=True,
#         top_p=0.95,
#         top_k=50,
#         temperature=0.75,
#         num_return_sequences=5,
#         pad_token_id=tokenizer.eos_token_id
#     )
#
#     #print the outputs
#     for i in range(len(chat_history_ids_list)):
#       output = tokenizer.decode(chat_history_ids_list[i][bot_input_ids.shape[-1]:], skip_special_tokens=True)
#       print(f"DialoGPT {i}: {output}")
#     choice_index = int(input("Choose the response you want for the next input: "))
#     chat_history_ids = torch.unsqueeze(chat_history_ids_list[choice_index], dim=0)

    #print the output
    output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(f"DialoGPT: {output}")

