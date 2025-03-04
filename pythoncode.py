import numpy as np

# Tracking Error
comparison_df["Squared_Diff"] = comparison_df["Weight_Difference"] ** 2
tracking_error = np.sqrt(comparison_df["Squared_Diff"].sum())

# Active Share
active_share = comparison_df["Weight_Difference"].abs().sum() / 2

# Calculate Portfolio and Benchmark Returns using Closing Prices
closing_prices_df['Daily_Return'] = closing_prices_df.groupby('Ticker')['Close'].pct_change()
portfolio_returns = closing_prices_df.merge(portfolio_df, on="Ticker")
benchmark_returns = closing_prices_df.merge(benchmark_df, on="Ticker")

# Portfolio & Benchmark Return Calculation
portfolio_returns['Weighted_Return'] = portfolio_returns['Daily_Return'] * portfolio_returns['Weight']
benchmark_returns['Weighted_Return'] = benchmark_returns['Daily_Return'] * benchmark_returns['Weight']

portfolio_return = portfolio_returns.groupby('Date')['Weighted_Return'].sum()
benchmark_return = benchmark_returns.groupby('Date')['Weighted_Return'].sum()

# Volatility & Sharpe Ratio
portfolio_volatility = portfolio_return.std()
sharpe_ratio = portfolio_return.mean() / portfolio_volatility




# Normalize weights
portfolio_df['Weight'] /= portfolio_df['Weight'].sum()
benchmark_df['Weight'] /= benchmark_df['Weight'].sum()

# Merge for comparison
comparison_df = portfolio_df.merge(benchmark_df, on="Ticker", suffixes=("_Portfolio", "_Benchmark"))
comparison_df["Weight_Difference"] = comparison_df["Weight_Portfolio"] - comparison_df["Weight_Benchmark"]





import numpy as np

# Tracking Error
comparison_df["Squared_Diff"] = comparison_df["Weight_Difference"] ** 2
tracking_error = np.sqrt(comparison_df["Squared_Diff"].sum())

# Active Share
active_share = comparison_df["Weight_Difference"].abs().sum() / 2

# Calculate Portfolio and Benchmark Returns using Closing Prices
closing_prices_df['Daily_Return'] = closing_prices_df.groupby('Ticker')['Close'].pct_change()
portfolio_returns = closing_prices_df.merge(portfolio_df, on="Ticker")
benchmark_returns = closing_prices_df.merge(benchmark_df, on="Ticker")

# Portfolio & Benchmark Return Calculation
portfolio_returns['Weighted_Return'] = portfolio_returns['Daily_Return'] * portfolio_returns['Weight']
benchmark_returns['Weighted_Return'] = benchmark_returns['Daily_Return'] * benchmark_returns['Weight']

portfolio_return = portfolio_returns.groupby('Date')['Weighted_Return'].sum()
benchmark_return = benchmark_returns.groupby('Date')['Weighted_Return'].sum()

# Volatility & Sharpe Ratio
portfolio_volatility = portfolio_return.std()
sharpe_ratio = portfolio_return.mean() / portfolio_volatility




commentary = f"""
Portfolio Analysis Report:
- Tracking Error: {tracking_error:.2%} (Deviation from benchmark)
- Active Share: {active_share:.2%} (Indicates how different the portfolio is)
- Portfolio Volatility: {portfolio_volatility:.2%}
- Sharpe Ratio: {sharpe_ratio:.2f}

Comparison with Benchmark:
- Overweight in: {', '.join(comparison_df[comparison_df['Weight_Difference'] > 0]['Ticker'].tolist())}
- Underweight in: {', '.join(comparison_df[comparison_df['Weight_Difference'] < 0]['Ticker'].tolist())}
"""
print(commentary)



################### LLM Commentary generation ######################

portfolio_stats = {
    "tracking_error": tracking_error,
    "active_share": active_share,
    "portfolio_volatility": portfolio_volatility,
    "sharpe_ratio": sharpe_ratio,
    "overweight": comparison_df[comparison_df['Weight_Difference'] > 0]['Ticker'].tolist(),
    "underweight": comparison_df[comparison_df['Weight_Difference'] < 0]['Ticker'].tolist(),
}



import openai

openai.api_key = "your_api_key"

prompt = f"""
Analyze the portfolio using the following statistics:
- Tracking Error: {portfolio_stats['tracking_error']:.2%}
- Active Share: {portfolio_stats['active_share']:.2%}
- Portfolio Volatility: {portfolio_stats['portfolio_volatility']:.2%}
- Sharpe Ratio: {portfolio_stats['sharpe_ratio']:.2f}
- Overweight Stocks: {', '.join(portfolio_stats['overweight'])}
- Underweight Stocks: {', '.join(portfolio_stats['underweight'])}

Provide a professional investment analysis commentary.
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

print(response["choices"][0]["message"]["content"])




Comparison: With vs. Without LLMs

Feature	Without LLM (Traditional)	With LLM
Accuracy	High, but depends on predefined logic	High, but depends on LLM training
Flexibility	Limited to predefined templates	Can generate varied and more natural language commentary
Customization	Requires manual effort for different styles	Can be fine-tuned with different prompts
Cost	Free (if using local Python tools)	Requires API cost (OpenAI, etc.)
Speed	Fast, real-time processing	Slightly slower due to API calls
Final Thoughts

If you need structured, highly controlled reports, use the traditional Python-based approach.
If you want more natural, flexible commentary, integrate an LLM model to generate investment insights.
