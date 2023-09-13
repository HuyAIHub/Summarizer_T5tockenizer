import torch
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import FastAPI, File, UploadFile,Form, HTTPException
import torch
import uvicorn
from transformers import T5ForConditionalGeneration, T5Tokenizer

if torch.cuda.is_available():       
    device = torch.device("cuda")

    print('There are %d GPU(s) available.' % torch.cuda.device_count())

    print('We will use the GPU:', torch.cuda.get_device_name(0))
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

model = T5ForConditionalGeneration.from_pretrained("NlpHUST/t5-small-vi-summarization")
tokenizer = T5Tokenizer.from_pretrained("NlpHUST/t5-small-vi-summarization")
model.to(device)


app = FastAPI()


@app.get("/") 
async def root():
    return {"message": "Summarizer"}

@app.post("/summarize_text",response_class=HTMLResponse)
def upload(src: str = Form(...)):
    tokenized_text = tokenizer.encode(src, return_tensors="pt").to(device)
    model.eval()
    summary_ids = model.generate(
                        tokenized_text,
                        max_length=256, 
                        num_beams=5,
                        repetition_penalty=2.5, 
                        length_penalty=1.0, 
                        early_stopping=True
                    )
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    if output:
        return JSONResponse({"message": output})
    else:
        raise HTTPException(status_code=500, detail="Error sending")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8686)