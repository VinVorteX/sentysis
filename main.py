from loaddata import load_data
from sentiment import sentiment
import argparse

def main():
    parser = argparse.ArgumentParser(description="Sentiment Analysis Tool with Custom Stop Words")
    parser.add_argument("filename", type=str, help="path to your CSV file")
    parser.add_argument("--stopwords", type=str, nargs="+", default=[], help="Custom stop words (comma-separated)")
    args = parser.parse_args()

    df = load_data(args.filename)

    if df is not None:
        stop_words = args.stopwords
        df['sentiment'] = df['text'].apply(lambda x: sentiment(x, stop_words))

        positive = len(df[df['sentiment'] > 0])
        negative = len(df[df['sentiment'] < 0])
        neutral = len(df[df['sentiment'] == 0])

        print("\nSentiment Analysis Summary")
        print(f"Positive: {positive}")
        print(f"Negative: {negative}")
        print(f"Neutral: {neutral}")

        print("\nSample Analyzed Entries")
        for i in range(min(3, len(df))):  # Ensure that there are at least 3 entries
            text = df.loc[i, 'text']
            sentiment_score = df.loc[i, 'sentiment']
            print(f"Text: {text}")
            print(f"Sentiment: {sentiment_score}")

if __name__ == "__main__":
    main()
