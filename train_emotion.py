import pandas as pd
from datasets import Dataset
from sklearn.preprocessing import MultiLabelBinarizer
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
import joblib

df = pd.read_csv("dreams_labeled.csv")
df["labels"] = df["emotion_labels"].str.split(";")
mlb = MultiLabelBinarizer()
Y = mlb.fit_transform(df["labels"])
joblib.dump(mlb, "label_encoder.joblib")

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

def preprocess(x):
    return tokenizer(x["dream_text"], truncation=True, padding="max_length", max_length=128)

ds = Dataset.from_pandas(df)
ds = ds.map(preprocess, batched=True)
ds = ds.add_column("labels", list(Y.astype(int)))

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=len(mlb.classes_)
)

args = TrainingArguments(output_dir="dream_emotion_model", num_train_epochs=1, per_device_train_batch_size=2)
trainer = Trainer(model=model, args=args, train_dataset=ds)
trainer.train()
trainer.save_model("dream_emotion_model")
