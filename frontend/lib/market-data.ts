export type Asset = {
  symbol: string;
  name: string;
  price: string;
  change: string;
  bias: "Bullish" | "Bearish" | "Neutral";
  confidence: number;
};

export const assets: Asset[] = [
  { symbol: "R_100", name: "Volatility 100 Index", price: "1,438.29", change: "+1.82%", bias: "Bullish", confidence: 88 },
  { symbol: "R_75", name: "Volatility 75 Index", price: "983.14", change: "-0.46%", bias: "Neutral", confidence: 63 },
  { symbol: "BOOM1000", name: "Boom 1000 Index", price: "12,984.90", change: "+0.92%", bias: "Bullish", confidence: 81 },
  { symbol: "CRASH500", name: "Crash 500 Index", price: "7,291.62", change: "-1.13%", bias: "Bearish", confidence: 76 }
];

export const chartSeries = [
  { time: "09:00", price: 1420, ema: 1417, rsi: 48 },
  { time: "09:15", price: 1424, ema: 1419, rsi: 52 },
  { time: "09:30", price: 1418, ema: 1420, rsi: 45 },
  { time: "09:45", price: 1431, ema: 1423, rsi: 58 },
  { time: "10:00", price: 1437, ema: 1427, rsi: 62 },
  { time: "10:15", price: 1430, ema: 1428, rsi: 55 },
  { time: "10:30", price: 1442, ema: 1433, rsi: 68 },
  { time: "10:45", price: 1438, ema: 1435, rsi: 61 }
];

export const signals = [
  { asset: "R_100", side: "Buy", entry: "1,435.80", exit: "1,462.00", confidence: 88, risk: "Medium" },
  { asset: "CRASH500", side: "Sell", entry: "7,306.20", exit: "7,184.00", confidence: 76, risk: "High" },
  { asset: "BOOM1000", side: "Buy", entry: "12,950.00", exit: "13,180.00", confidence: 81, risk: "Medium" }
];

