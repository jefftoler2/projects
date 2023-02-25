{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from pandas.tseries.holiday import USFederalHolidayCalendar as calendar"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Utils "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "def change_label(x):\n",
    "    if x == \"Long\":\n",
    "        return 1\n",
    "    else:\n",
    "        return 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_data(df):\n",
    "    df = df[df[\"Date\"].dt.weekday < 5].reset_index(drop = True)\n",
    "    df.set_index(\"Date\", inplace = True, drop = True)\n",
    "    df = df.between_time(\"9:00\", \"16:00\")\n",
    "    df.reset_index(inplace = True)\n",
    "    holidays = calendar().holidays(start = \"1998-01-02\",end = \"2020-12-31\") \n",
    "    mask = df[\"Date\"].isin(holidays)\n",
    "    newdf = df[~mask].copy()\n",
    "    newdf = newdf.fillna(method = \"ffill\")\n",
    "    return newdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def label_data(x):\n",
    "    if x[\"Close\"] < x[\"Next Day Close\"]: \n",
    "        return \"Long\"\n",
    "    else:\n",
    "        return \"Short\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Time</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:31</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.89</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "      <td>35388</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:32</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.89</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.89</td>\n",
       "      <td>43580</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:33</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.89</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "      <td>55048</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:34</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.89</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "      <td>15731</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:35</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.89</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "      <td>76346</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date   Time   Open   High    Low  Close  Volume\n",
       "0  01/02/1998  09:31  31.85  31.89  31.85  31.85   35388\n",
       "1  01/02/1998  09:32  31.87  31.89  31.85  31.89   43580\n",
       "2  01/02/1998  09:33  31.87  31.89  31.85  31.85   55048\n",
       "3  01/02/1998  09:34  31.85  31.89  31.85  31.85   15731\n",
       "4  01/02/1998  09:35  31.87  31.89  31.85  31.85   76346"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "col_name = [\"Date\", \"Time\", \"Open\", \"High\", \"Low\", \"Close\", \"Volume\"]\n",
    "df = pd.read_csv(\"IBM_adjusted.txt\", names=col_name, header = 0)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date      0\n",
       "Time      0\n",
       "Open      0\n",
       "High      0\n",
       "Low       0\n",
       "Close     0\n",
       "Volume    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Time</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:31</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:32</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:33</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:34</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>01/02/1998</td>\n",
       "      <td>09:35</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date   Time   Open  Close\n",
       "0  01/02/1998  09:31  31.85  31.85\n",
       "1  01/02/1998  09:32  31.87  31.89\n",
       "2  01/02/1998  09:33  31.87  31.85\n",
       "3  01/02/1998  09:34  31.85  31.85\n",
       "4  01/02/1998  09:35  31.87  31.85"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop([\"High\", \"Low\", \"Volume\"], axis = 1, inplace = True)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Date\"] = pd.to_datetime(df[\"Date\"] + \" \" + df[\"Time\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998-01-02 09:31:00</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1998-01-02 09:32:00</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1998-01-02 09:33:00</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1998-01-02 09:34:00</td>\n",
       "      <td>31.85</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1998-01-02 09:35:00</td>\n",
       "      <td>31.87</td>\n",
       "      <td>31.85</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Date   Open  Close\n",
       "0 1998-01-02 09:31:00  31.85  31.85\n",
       "1 1998-01-02 09:32:00  31.87  31.89\n",
       "2 1998-01-02 09:33:00  31.87  31.85\n",
       "3 1998-01-02 09:34:00  31.85  31.85\n",
       "4 1998-01-02 09:35:00  31.87  31.85"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop([\"Time\"], axis = 1, inplace = True)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv(\"data_ready.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2436174"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998-01-02 09:00:00</td>\n",
       "      <td>31.910000</td>\n",
       "      <td>31.914828</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1998-01-02 10:00:00</td>\n",
       "      <td>31.883220</td>\n",
       "      <td>31.884746</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1998-01-02 11:00:00</td>\n",
       "      <td>32.014576</td>\n",
       "      <td>32.015085</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1998-01-02 12:00:00</td>\n",
       "      <td>32.043966</td>\n",
       "      <td>32.045517</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1998-01-02 13:00:00</td>\n",
       "      <td>32.032000</td>\n",
       "      <td>32.033000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Date       Open      Close\n",
       "0 1998-01-02 09:00:00  31.910000  31.914828\n",
       "1 1998-01-02 10:00:00  31.883220  31.884746\n",
       "2 1998-01-02 11:00:00  32.014576  32.015085\n",
       "3 1998-01-02 12:00:00  32.043966  32.045517\n",
       "4 1998-01-02 13:00:00  32.032000  32.033000"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.groupby(pd.Grouper(key = \"Date\", freq = \"1h\")).mean().reset_index()\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "204371"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998-01-02 09:00:00</td>\n",
       "      <td>31.910000</td>\n",
       "      <td>31.914828</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1998-01-02 10:00:00</td>\n",
       "      <td>31.883220</td>\n",
       "      <td>31.884746</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1998-01-02 11:00:00</td>\n",
       "      <td>32.014576</td>\n",
       "      <td>32.015085</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1998-01-02 12:00:00</td>\n",
       "      <td>32.043966</td>\n",
       "      <td>32.045517</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1998-01-02 13:00:00</td>\n",
       "      <td>32.032000</td>\n",
       "      <td>32.033000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Date       Open      Close\n",
       "0 1998-01-02 09:00:00  31.910000  31.914828\n",
       "1 1998-01-02 10:00:00  31.883220  31.884746\n",
       "2 1998-01-02 11:00:00  32.014576  32.015085\n",
       "3 1998-01-02 12:00:00  32.043966  32.045517\n",
       "4 1998-01-02 13:00:00  32.032000  32.033000"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Open\"] = df[\"Open\"].replace(to_replace = 0, method = \"ffill\")\n",
    "\n",
    "df[\"Close\"] = df[\"Close\"].replace(to_replace = 0, method = \"ffill\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998-01-02 09:00:00</td>\n",
       "      <td>31.910000</td>\n",
       "      <td>31.914828</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1998-01-02 10:00:00</td>\n",
       "      <td>31.883220</td>\n",
       "      <td>31.884746</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1998-01-02 11:00:00</td>\n",
       "      <td>32.014576</td>\n",
       "      <td>32.015085</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1998-01-02 12:00:00</td>\n",
       "      <td>32.043966</td>\n",
       "      <td>32.045517</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1998-01-02 13:00:00</td>\n",
       "      <td>32.032000</td>\n",
       "      <td>32.033000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48651</th>\n",
       "      <td>2021-04-26 12:00:00</td>\n",
       "      <td>142.703843</td>\n",
       "      <td>142.703290</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48652</th>\n",
       "      <td>2021-04-26 13:00:00</td>\n",
       "      <td>142.275947</td>\n",
       "      <td>142.269082</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48653</th>\n",
       "      <td>2021-04-26 14:00:00</td>\n",
       "      <td>141.966905</td>\n",
       "      <td>141.963307</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48654</th>\n",
       "      <td>2021-04-26 15:00:00</td>\n",
       "      <td>141.807362</td>\n",
       "      <td>141.803703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48655</th>\n",
       "      <td>2021-04-26 16:00:00</td>\n",
       "      <td>141.450000</td>\n",
       "      <td>141.404286</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>48656 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Date        Open       Close\n",
       "0     1998-01-02 09:00:00   31.910000   31.914828\n",
       "1     1998-01-02 10:00:00   31.883220   31.884746\n",
       "2     1998-01-02 11:00:00   32.014576   32.015085\n",
       "3     1998-01-02 12:00:00   32.043966   32.045517\n",
       "4     1998-01-02 13:00:00   32.032000   32.033000\n",
       "...                   ...         ...         ...\n",
       "48651 2021-04-26 12:00:00  142.703843  142.703290\n",
       "48652 2021-04-26 13:00:00  142.275947  142.269082\n",
       "48653 2021-04-26 14:00:00  141.966905  141.963307\n",
       "48654 2021-04-26 15:00:00  141.807362  141.803703\n",
       "48655 2021-04-26 16:00:00  141.450000  141.404286\n",
       "\n",
       "[48656 rows x 3 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cleandf = clean_data(df)\n",
    "cleandf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Next Day Close</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998-01-02 09:00:00</td>\n",
       "      <td>31.910000</td>\n",
       "      <td>31.914828</td>\n",
       "      <td>31.884746</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1998-01-02 10:00:00</td>\n",
       "      <td>31.883220</td>\n",
       "      <td>31.884746</td>\n",
       "      <td>32.015085</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1998-01-02 11:00:00</td>\n",
       "      <td>32.014576</td>\n",
       "      <td>32.015085</td>\n",
       "      <td>32.045517</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1998-01-02 12:00:00</td>\n",
       "      <td>32.043966</td>\n",
       "      <td>32.045517</td>\n",
       "      <td>32.033000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1998-01-02 13:00:00</td>\n",
       "      <td>32.032000</td>\n",
       "      <td>32.033000</td>\n",
       "      <td>31.925185</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Date       Open      Close  Next Day Close\n",
       "0 1998-01-02 09:00:00  31.910000  31.914828       31.884746\n",
       "1 1998-01-02 10:00:00  31.883220  31.884746       32.015085\n",
       "2 1998-01-02 11:00:00  32.014576  32.015085       32.045517\n",
       "3 1998-01-02 12:00:00  32.043966  32.045517       32.033000\n",
       "4 1998-01-02 13:00:00  32.032000  32.033000       31.925185"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cleandf[\"Next Day Close\"] = cleandf[\"Close\"].shift(-1)\n",
    "cleandf.dropna(inplace = True)\n",
    "cleandf.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Next Day Close</th>\n",
       "      <th>Label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998-01-02 09:00:00</td>\n",
       "      <td>31.910000</td>\n",
       "      <td>31.914828</td>\n",
       "      <td>31.884746</td>\n",
       "      <td>Short</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1998-01-02 10:00:00</td>\n",
       "      <td>31.883220</td>\n",
       "      <td>31.884746</td>\n",
       "      <td>32.015085</td>\n",
       "      <td>Long</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1998-01-02 11:00:00</td>\n",
       "      <td>32.014576</td>\n",
       "      <td>32.015085</td>\n",
       "      <td>32.045517</td>\n",
       "      <td>Long</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1998-01-02 12:00:00</td>\n",
       "      <td>32.043966</td>\n",
       "      <td>32.045517</td>\n",
       "      <td>32.033000</td>\n",
       "      <td>Short</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1998-01-02 13:00:00</td>\n",
       "      <td>32.032000</td>\n",
       "      <td>32.033000</td>\n",
       "      <td>31.925185</td>\n",
       "      <td>Short</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Date       Open      Close  Next Day Close  Label\n",
       "0 1998-01-02 09:00:00  31.910000  31.914828       31.884746  Short\n",
       "1 1998-01-02 10:00:00  31.883220  31.884746       32.015085   Long\n",
       "2 1998-01-02 11:00:00  32.014576  32.015085       32.045517   Long\n",
       "3 1998-01-02 12:00:00  32.043966  32.045517       32.033000  Short\n",
       "4 1998-01-02 13:00:00  32.032000  32.033000       31.925185  Short"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cleandf[\"Label\"] = cleandf.apply(lambda x: label_data(x), axis = 1)\n",
    "cleandf.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "cleandf.drop([\"Next Day Close\", \"Close\"], axis = 1, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import MinMaxScaler\n",
    "scaler = MinMaxScaler()\n",
    "train_data = cleandf[cleandf[\"Date\"] < \"2017\"]\n",
    "test_data = cleandf[cleandf[\"Date\"] >= \"2017\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9007"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(test_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train = train_data.drop([\"Label\"], axis = 1)\n",
    "y_train = train_data[\"Label\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998-01-02 09:00:00</td>\n",
       "      <td>31.910000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1998-01-02 10:00:00</td>\n",
       "      <td>31.883220</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1998-01-02 11:00:00</td>\n",
       "      <td>32.014576</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1998-01-02 12:00:00</td>\n",
       "      <td>32.043966</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1998-01-02 13:00:00</td>\n",
       "      <td>32.032000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39643</th>\n",
       "      <td>2016-12-30 12:00:00</td>\n",
       "      <td>137.147500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39644</th>\n",
       "      <td>2016-12-30 13:00:00</td>\n",
       "      <td>137.042034</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39645</th>\n",
       "      <td>2016-12-30 14:00:00</td>\n",
       "      <td>136.823500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39646</th>\n",
       "      <td>2016-12-30 15:00:00</td>\n",
       "      <td>136.694500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39647</th>\n",
       "      <td>2016-12-30 16:00:00</td>\n",
       "      <td>136.713333</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>39648 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Date        Open\n",
       "0     1998-01-02 09:00:00   31.910000\n",
       "1     1998-01-02 10:00:00   31.883220\n",
       "2     1998-01-02 11:00:00   32.014576\n",
       "3     1998-01-02 12:00:00   32.043966\n",
       "4     1998-01-02 13:00:00   32.032000\n",
       "...                   ...         ...\n",
       "39643 2016-12-30 12:00:00  137.147500\n",
       "39644 2016-12-30 13:00:00  137.042034\n",
       "39645 2016-12-30 14:00:00  136.823500\n",
       "39646 2016-12-30 15:00:00  136.694500\n",
       "39647 2016-12-30 16:00:00  136.713333\n",
       "\n",
       "[39648 rows x 2 columns]"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_test = test_data.drop([\"Label\"], axis = 1)\n",
    "y_test = test_data[\"Label\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train_scaled = scaler.fit_transform(x_train[\"Open\"].values.reshape(-1,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_test_scaled = scaler.transform(x_test[\"Open\"].values.reshape(-1,1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# create/reshape data for prediction, each time use the previous 20 days. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x_train  (39628, 20)\n",
      "y_train  (39628,)\n"
     ]
    }
   ],
   "source": [
    "x_train_reshaped = []\n",
    "y_train_reshaped = []\n",
    "y_train_binary = y_train.apply(lambda x : change_label(x))\n",
    "for i in range(20, len(x_train)):\n",
    "    x_train_reshaped.append(x_train_scaled[i - 19: i + 1, 0])\n",
    "    y_train_reshaped.append(y_train_binary[i])\n",
    "x_train_reshaped = np.array(x_train_reshaped)\n",
    "y_train_reshaped = np.array(y_train_reshaped)\n",
    "print(\"x_train \", x_train_reshaped.shape)\n",
    "print(\"y_train \", y_train_reshaped.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# LSTM only accepts values in 3-dimensions, have to reshape the data "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train_reshaped = np.reshape(x_train_reshaped, (x_train_reshaped.shape[0], x_train_reshaped.shape[1], 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x_train  (39628, 20, 1)\n"
     ]
    }
   ],
   "source": [
    "print(\"x_train \", x_train_reshaped.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# building LSTM neural net"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "from keras.models import Sequential\n",
    "from keras.layers import Dense, LSTM, Dropout\n",
    "import tensorflow as tf \n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.metrics import mean_squared_error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = Sequential()\n",
    "model.add(LSTM(units = 100, activation = \"tanh\", return_sequences = True, input_shape = (x_train_reshaped.shape[1], 1)))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(LSTM(units = 50, activation = \"tanh\", return_sequences = True))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(LSTM(units = 25, activation = \"tanh\"))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(Dense(units = 1, activation = \"sigmoid\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.compile(optimizer = \"adam\", loss = \"binary_crossentropy\", metrics = [\"accuracy\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/15\n",
      "1239/1239 [==============================] - 30s 22ms/step - loss: 0.6934 - accuracy: 0.5098\n",
      "Epoch 2/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6929 - accuracy: 0.5140\n",
      "Epoch 3/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6921 - accuracy: 0.5230\n",
      "Epoch 4/15\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 0.6928 - accuracy: 0.5159\n",
      "Epoch 5/15\n",
      "1239/1239 [==============================] - 25s 21ms/step - loss: 0.6924 - accuracy: 0.5210\n",
      "Epoch 6/15\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 0.6927 - accuracy: 0.5149\n",
      "Epoch 7/15\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 0.6928 - accuracy: 0.5087\n",
      "Epoch 8/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6925 - accuracy: 0.5181\n",
      "Epoch 9/15\n",
      "1239/1239 [==============================] - 25s 21ms/step - loss: 0.6924 - accuracy: 0.5205\n",
      "Epoch 10/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6923 - accuracy: 0.5194\n",
      "Epoch 11/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6928 - accuracy: 0.5147\n",
      "Epoch 12/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6927 - accuracy: 0.5163\n",
      "Epoch 13/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6929 - accuracy: 0.5123\n",
      "Epoch 14/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6928 - accuracy: 0.5150\n",
      "Epoch 15/15\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 0.6922 - accuracy: 0.5222\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<tensorflow.python.keras.callbacks.History at 0x7f854c621190>"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train_reshaped, y_train_reshaped, epochs = 15, batch_size = 32, verbose = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x_test  (8987, 20)\n",
      "y_test  (8987,)\n"
     ]
    }
   ],
   "source": [
    "x_test_reshaped = []\n",
    "y_test_reshaped = []\n",
    "y_test_binary = y_test.apply(lambda x : change_label(x))\n",
    "y_test_binary.reset_index(drop = True, inplace = True)\n",
    "for i in range(20, len(x_test)):\n",
    "    x_test_reshaped.append(x_test_scaled[i - 19: i + 1, 0])\n",
    "    y_test_reshaped.append(y_test_binary[i])\n",
    "x_test_reshaped = np.array(x_test_reshaped)\n",
    "y_test_reshaped = np.array(y_test_reshaped)\n",
    "print(\"x_test \", x_test_reshaped.shape)\n",
    "print(\"y_test \", y_test_reshaped.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_test_reshaped = np.reshape(x_test_reshaped, (x_test_reshaped.shape[0], x_test_reshaped.shape[1], 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = model.predict(x_test_reshaped)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions_label = np.where(predictions > 0.5, 1, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5195282074107044"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test_reshaped, predictions_label)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Attempt to predict price, transforming to regression problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x_train  (39628, 20)\n",
      "y_train  (39628,)\n"
     ]
    }
   ],
   "source": [
    "x_train_reshaped = []\n",
    "y_train_reshaped = []\n",
    "for i in range(20, len(x_train)):\n",
    "    x_train_reshaped.append(x_train_scaled[i - 20: i, 0])\n",
    "    y_train_reshaped.append(x_train_scaled[i, 0])\n",
    "x_train_reshaped = np.array(x_train_reshaped)\n",
    "y_train_reshaped = np.array(y_train_reshaped)\n",
    "print(\"x_train \", x_train_reshaped.shape)\n",
    "print(\"y_train \", y_train_reshaped.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train_reshaped = np.reshape(x_train_reshaped, (x_train_reshaped.shape[0], x_train_reshaped.shape[1], 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = Sequential()\n",
    "model.add(LSTM(units = 100, activation = \"tanh\", return_sequences = True, input_shape = (x_train_reshaped.shape[1], 1)))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(LSTM(units = 50, activation = \"tanh\", return_sequences = True))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(LSTM(units = 25, activation = \"tanh\"))\n",
    "model.add(Dropout(0.2))\n",
    "model.add(Dense(units = 1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "model.compile(optimizer = \"adam\", loss = \"mse\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/25\n",
      "1239/1239 [==============================] - 30s 21ms/step - loss: 0.0081\n",
      "Epoch 2/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 0.0018\n",
      "Epoch 3/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 0.0012\n",
      "Epoch 4/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 9.7148e-04\n",
      "Epoch 5/25\n",
      "1239/1239 [==============================] - 27s 22ms/step - loss: 0.0010\n",
      "Epoch 6/25\n",
      "1239/1239 [==============================] - 25s 21ms/step - loss: 9.4463e-04\n",
      "Epoch 7/25\n",
      "1239/1239 [==============================] - 25s 21ms/step - loss: 9.5801e-04\n",
      "Epoch 8/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 9.7350e-04\n",
      "Epoch 9/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 9.3536e-04\n",
      "Epoch 10/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 9.3303e-04\n",
      "Epoch 11/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 9.4472e-04\n",
      "Epoch 12/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 9.2813e-04\n",
      "Epoch 13/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 9.0522e-04\n",
      "Epoch 14/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 8.9168e-04\n",
      "Epoch 15/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 9.0320e-04\n",
      "Epoch 16/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 9.2049e-04\n",
      "Epoch 17/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 8.9542e-04\n",
      "Epoch 18/25\n",
      "1239/1239 [==============================] - 25s 21ms/step - loss: 8.9365e-04\n",
      "Epoch 19/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 8.8169e-04\n",
      "Epoch 20/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 8.9785e-04\n",
      "Epoch 21/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 8.7250e-04\n",
      "Epoch 22/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 8.7519e-04\n",
      "Epoch 23/25\n",
      "1239/1239 [==============================] - 25s 20ms/step - loss: 8.8089e-04\n",
      "Epoch 24/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 8.8464e-04\n",
      "Epoch 25/25\n",
      "1239/1239 [==============================] - 26s 21ms/step - loss: 8.3617e-04\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<tensorflow.python.keras.callbacks.History at 0x7f857b26e7f0>"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train_reshaped, y_train_reshaped, epochs = 25, batch_size = 32, verbose = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x_test  (8987, 20)\n",
      "y_test  (8987,)\n"
     ]
    }
   ],
   "source": [
    "x_test_reshaped = []\n",
    "y_test_reshaped = []\n",
    "for i in range(20, len(x_test)):\n",
    "    x_test_reshaped.append(x_test_scaled[i - 20: i, 0])\n",
    "    y_test_reshaped.append(x_test_scaled[i, 0])\n",
    "x_test_reshaped = np.array(x_test_reshaped)\n",
    "y_test_reshaped = np.array(y_test_reshaped)\n",
    "print(\"x_test \", x_test_reshaped.shape)\n",
    "print(\"y_test \", y_test_reshaped.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_test_reshaped = np.reshape(x_test_reshaped, (x_test_reshaped.shape[0], x_test_reshaped.shape[1], 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = model.predict(x_test_reshaped)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_test_reshaped = scaler.inverse_transform(y_test_reshaped.reshape(-1,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = scaler.inverse_transform(predictions.reshape(-1,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "rmse = np.sqrt(mean_squared_error(y_test_reshaped, predictions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.1684769000492001"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rmse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7f858968ba30>"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABIQAAAI/CAYAAAAGDwK6AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAEAAElEQVR4nOzdd3hb5dnH8e/RsizvFceJkzh7b0YggSSMACVQ9iij7FWgLQ0Fyg7Q8pZRRlmh7L0po0CAQMIIKyRkkT2dbTvelrXO+8ejo+EVD8mypftzXVySjo6kJ8aWdH7nfu5H03UdIYQQQgghhBBCCJE4TLEegBBCCCGEEEIIIYToXBIICSGEEEIIIYQQQiQYCYSEEEIIIYQQQgghEowEQkIIIYQQQgghhBAJRgIhIYQQQgghhBBCiAQjgZAQQgghhBBCCCFEgrHEegAAubm5elFRUayHIYQQQgghhBBCCBE3Fi1aVKLrel5T93WJQKioqIiffvop1sMQQgghhBBCCCGEiBuapm1u7j6ZMiaEEEIIIYQQQgiRYCQQEkIIIYQQQgghhEgwEggJIYQQQgghhBBCJJgu0UNICCGEEEIIIYTortxuN8XFxTidzlgPRSQou91OYWEhVqu11Y+RQEgIIYQQQgghhOiA4uJi0tLSKCoqQtO0WA9HJBhd1yktLaW4uJj+/fu3+nEyZUwIIYQQQgghhOgAp9NJTk6OhEEiJjRNIycnp80VahIICSGEEEIIIYQQHSRhkIil9vz+SSAkhBBCCCGEEEIkuKKiIkpKSlrcbjabGTduHGPHjmXChAl8++23AGzatAlN07j55psDjyspKcFqtXLllVe26vU3bdrEyy+/HPHxt8fjjz/O888/H5Hn6sokEBJCCCGEEEIIIeKEruv4fL6oPHdycjJLlizhl19+4R//+Ac33HBD4L4BAwbwwQcfBG6/8cYbjBw5stXP3dFAKFI8Hg+XXXYZ5557bqyHEnUSCAkhhBBCCCGEEN3Ypk2bGD58OFdccQUTJkxg69at3HPPPey///6MGTOGW2+9NbDvCSecwMSJExk5ciRz5sxp92tWVlaSlZUVuJ2cnMzw4cP56aefAHjttdc47bTTmnzs/PnzGTduHOPGjWP8+PFUVVVx/fXX89VXXzFu3Dj+9a9/4XQ6Of/88xk9ejTjx4/niy++AMDr9TJr1ixGjx7NmDFjePjhh8Oeu66ujqOPPponn3yy0eumpqbyl7/8hQkTJnD44YezZ88eAKZNm8bf/vY3pk6dyoMPPshtt93GvffeC8C6des44ogjAlVR69evB2j259udyCpjQgghhBBCCCFEN7d69WqeeeYZHn30UebOncvatWv54Ycf0HWd448/ngULFnDooYfy9NNPk52dTV1dHfvvvz8nn3wyOTk5rXqNuro6xo0bh9PpZMeOHcybNy/s/jPOOINXX32Vnj17Yjab6dWrF9u3b2/0PPfeey+PPPIIkydPprq6Grvdzt133829994bqDK67777AFi2bBmrVq1ixowZrFmzhmeeeYaNGzeyePFiLBYLZWVlgeetrq7mjDPO4Nxzz22ywqempoYJEyZw3333MXv2bG6//Xb+/e9/A1BeXs78+fMBuO222wKPOeuss7j++us58cQTcTqd+Hy+Fn++3YkEQkIIIYQQQgghRIT86U+wZElkn3PcOHjggZb36devH5MmTQJg7ty5zJ07l/HjxwMqKFm7di2HHnooDz30EO+88w4AW7duZe3ata0OhIwpYwALFy7k3HPPZfny5YH7jz76aG6++Wby8/M5/fTTm32eyZMnc80113DWWWdx0kknUVhY2Gifr7/+mquuugqAYcOG0a9fP9asWcNnn33GZZddhsWi4ozs7OzAY37729/y17/+lbPOOqvJ1zWZTIFxnX322Zx00kmB+5oab1VVFdu2bePEE08EwG63Ay3/fLsTCYSEEEIIIYQQQohuLiUlJXBd13VuuOEGLr300rB9vvzySz777DMWLlyIw+Fg2rRpbV6q3HDQQQdRUlISmHYFYLPZmDhxIvfddx8rVqzg/fffb/Kx119/Pcceeyz/+9//mDRpEp999lmjfXRdb/Kxuq43u6LW5MmT+eijj/jd737XqlW3QvcJ/fm1ZgxN/Xy7GwmEhBBCCCGEEEKICNlXJU9nOOqoo7j55ps566yzSE1NZdu2bVitVioqKsjKysLhcLBq1Sq+++67dr/GqlWr8Hq95OTkUFtbG9j+l7/8halTp7ZYdbR+/XpGjx7N6NGjWbhwIatWraJPnz5UVVUF9jn00EN56aWXOOyww1izZg1btmxh6NChzJgxg8cff5xp06YFpowZVUKzZ8/mjjvu4IorruCxxx5r9Lo+n48333yTM844g5dffpkpU6a0+G9MT0+nsLCQd999lxNOOIH6+nq8Xm+zP98ePXq09ccYUxIICSGEEEIIIYQQcWTGjBn8+uuvHHTQQYBqpvziiy9y9NFH8/jjjzNmzBiGDh0amGLWWkYPIVBVMs899xxmszlsn5EjR+5zdbEHHniAL774ArPZzIgRIzjmmGMwmUxYLBbGjh3LeeedxxVXXMFll13G6NGjsVgsPPvssyQlJXHRRRexZs0axowZg9Vq5eKLLw5b2v6BBx7gggsu4K9//Sv//Oc/w143JSWFFStWMHHiRDIyMnjttdf2+W9+4YUXuPTSS7nllluwWq288cYbzf58u1sgpDVXAtWZ9ttvP93oRC6EEEIIIYQQQnQnv/76K8OHD4/1MMQ+pKamUl1dHethRE1Tv4eapi3SdX2/pvaXZeeFEEIIIYQQQgghEowEQkIIIYQQQgghhIh78Vwd1B4SCAkhhBBCCCGEEEIkGAmEhBBCCCGEEEIIIRKMBEJCCCGEEEIIIYQQCUYCISGEEEIIIYQQQogEI4FQN+X1wjHHwLx5sR6JEEIIIYQQQoh48uWXXzJz5kwA3nvvPe6+++5m9y0vL+fRRx9t82vcdttt3HvvvS1uP++88+jfvz/jxo1j2LBh3H777YH9pk2bRt++fdF1PbDthBNOIDU1tdVjeOCBB6itrW3z2Fsaf3ts376dU045JSLP1RYSCHVTe/fCxx/DySc3v09NDfznPxDy9yGEEEIIIYQQIkF5vd42P+b444/n+uuvb/b+9gZCrXXPPfewZMkSlixZwnPPPcfGjRsD92VmZvLNN98ExrFjx442PXdHAqFI8Xg89OrVizfffLPTX1sCoW7K49n3PpdfDhdfDN99F/3xCCGEEEIIIYSIjU2bNjFs2DB+//vfM2bMGE455ZRA0FFUVMTs2bOZMmUKb7zxBnPnzuWggw5iwoQJnHrqqYGl2D/++GOGDRvGlClTePvttwPP/eyzz3LllVcCsGvXLk488UTGjh3L2LFj+fbbb7n++utZv34948aN49prrwVUiLP//vszZswYbr311sBz3XXXXQwdOpQjjjiC1atXt+nf6HQ6AUhJSQlsO+OMM3j11VcBePvttznppJOafGxNTQ3HHnssY8eOZdSoUbz22ms89NBDbN++nenTpzN9+nQAXnnlFUaPHs2oUaO47rrrAo//+OOPmTBhAmPHjuXwww9v9PxPPvkkxxxzDHV1dWHbzzvvPC677DIOOeQQhgwZwgcffBD4mZ566qkcd9xxzJgxg02bNjFq1ChAhXazZs1i9OjRjBkzhocffhiARYsWMXXqVCZOnMhRRx3V5vCrKZYOP4OICeP3rKXqn59+UpetCY+EEEIIIYQQQnRfq1ev5qmnnmLy5MlccMEFPProo8yaNQsAu93O119/TUlJCSeddBKfffYZKSkp/N///R/3338/f/3rX7n44ouZN28egwYN4vTTT2/yNa6++mqmTp3KO++8g9frpbq6mrvvvpvly5ezZMkSAObOncvatWv54Ycf0HWd448/ngULFpCSksKrr77K4sWL8Xg8TJgwgYkTJ+7z33Xttddy5513sm7dOq6++mp69OgRuO/www/n4osvxuv18uqrrzJnzhzuuOOORs/x8ccf06tXLz788EMAKioqyMjI4P777+eLL74gNzeX7du3c91117Fo0SKysrKYMWMG7777LpMnT+biiy9mwYIF9O/fn7KysrDn/ve//83cuXN59913SUpKavTamzZtYv78+axfv57p06ezbt06ABYuXMjSpUvJzs5m06ZNgf3nzJnDxo0bWbx4MRaLhbKyMtxuN1dddRX//e9/ycvL47XXXuPGG2/k6aef3ufPryUSCHVT69c33rZlC/TrB489BpddBm632l5V1bljE0IIIYQQQoiE9ac/gT8ciZhx4+CBB1rcpU+fPkyePBmAs88+m4ceeigQCBkBz3fffcfKlSsD+7lcLg466CBWrVpF//79GTx4cODxc+bMafQa8+bN4/nnnwfAbDaTkZHB3r17w/aZO3cuc+fOZfz48QBUV1ezdu1aqqqqOPHEE3E4HICaitYa99xzD6eccgrV1dUcfvjhfPvttxx88MGBMUyZMoXXXnuNuro6ioqKmnyO0aNHM2vWLK677jpmzpzJIYcc0mifH3/8kWnTppGXlwfAWWedxYIFCzCbzRx66KH0798fgOzs7MBjXnjhBQoLC3n33XexWq1NvvZpp52GyWRi8ODBDBgwgFWrVgFw5JFHhj2X4bPPPuOyyy7DYrEEXm/58uUsX76cI488ElBVRAUFBa358bVIpox1U/fdpy4rKoLb+vVTl5dfri5dLnXZoGpNCCGEEEIIIUSc0TSt2dvGNCtd1znyyCMDPXlW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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(1,1,figsize = (20, 10))\n",
    "plt.plot(y_test_reshaped, color = \"blue\", label = \"real IBM stock price\")\n",
    "plt.plot(predictions, color = \"red\", label = \"predicted IBM stock price\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.legend.Legend at 0x7f8589a18520>"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABI4AAAI/CAYAAAARLZJzAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAADMiUlEQVR4nOzdd3QU9dfH8feE0AKoNBEEEgsCQighFqSqgAVFUbEQFVRA7A0pYkdswCNiB0RQV7H8FCxIUyyIDRQQFEEkVKUqLbQk8/xxCQSygZTdnS2f1zmcTWZ3Z25Cstm5c+/9Oq7rIiIiIiIiIiIicrA4rwMQEREREREREZHwpMSRiIiIiIiIiIj4pcSRiIiIiIiIiIj4pcSRiIiIiIiIiIj4pcSRiIiIiIiIiIj4pcSRiIiIiIiIiIj4Fe91AIVRpUoVNykpyeswRERERERERESixpw5cza4rlvV330RlThKSkpi9uzZXochIiIiIiIiIhI1HMdZnt99alUTERERERERERG/lDgSERERERERERG/lDgSERERERERERG/ImrGkYiIiIiIiEik2rNnD6tWrWLnzp1ehyIxqkyZMtSsWZOSJUsW+DlKHImIiIiIiIiEwKpVq6hQoQJJSUk4juN1OBJjXNdl48aNrFq1iuOOO67Az1OrmoiIiIiIiEgI7Ny5k8qVKytpJJ5wHIfKlSsXuuJNiSMRERERERGREFHSSLxUlJ8/JY5EREREREREpECSkpLYsGHDIbeXKFGCJk2a0LhxY1JSUpg1axYA6enpOI7DAw88sO95GzZsoGTJktx6660FOn56ejpvvfVWwOMvipdffpnXX389IPsKZ0ociYiIiIiIiMQY13XJzs4Oyr7Lli3L3LlzmTdvHk888QQDBgzYd9/xxx/PJ598su/z9957jwYNGhR438VNHAVKZmYmvXv35tprr/U6lKBT4khEREREREQkBqSnp1O/fn1uvvlmUlJSWLlyJUOGDOGUU06hUaNGPPTQQ/see/HFF9OsWTMaNGjAyJEji3zMLVu2ULFixX2fly1blvr16zN79mwA3nnnHS6//HK/z/3qq69o0qQJTZo0oWnTpmzdupX+/fvzzTff0KRJE5555hl27tzJddddR3JyMk2bNmXGjBkAZGVl0adPH5KTk2nUqBHPPffcAfvesWMH5557LqNGjcpz3PLly3PPPfeQkpLC2Wefzfr16wFo27Yt9913H23atOHZZ5/l4YcfZujQoQD8+eeftGvXbl+V1dKlSwHy/f5GEq2qJiIiIiIiIhIj/vjjD1577TVefPFFpk6dypIlS/jxxx9xXZdOnTrx9ddf07p1a8aMGUOlSpXYsWMHp5xyCpdeeimVK1cu0DF27NhBkyZN2LlzJ3///TdffPHFAfdfeeWVjB8/nmOOOYYSJUpQo0YN1qxZk2c/Q4cO5YUXXqBFixZs27aNMmXK8OSTTzJ06NB9VUvDhg0D4Ndff2XRokV06NCBxYsX89prr7Fs2TJ++eUX4uPj2bRp0779btu2jSuvvJJrr73Wb8XQ9u3bSUlJYdiwYTz66KM88sgjPP/88wD8999/fPXVVwA8/PDD+56TlpZG//796dy5Mzt37iQ7O/uQ399IosSRiIiIiIiISIjdeSfMnRvYfTZpAsOHH/oxiYmJnH766QBMnTqVqVOn0rRpU8ASKkuWLKF169aMGDGCDz/8EICVK1eyZMmSAieOclrVAL777juuvfZaFixYsO/+c889lwceeIBq1apxxRVX5LufFi1acPfdd5OWlsYll1xCzZo18zxm5syZ3HbbbQDUq1ePxMREFi9ezPTp0+nduzfx8Zb2qFSp0r7nXHTRRfTt25e0tDS/x42Li9sX19VXX80ll1yy7z5/8W7dupXVq1fTuXNnAMqUKQMc+vsbSZQ4EhEREREREYkR5cqV2/ex67oMGDCAG2+88YDHfPnll0yfPp3vvvuOhIQE2rZtW+gl3HM0b96cDRs27Gv3AihVqhTNmjVj2LBhLFy4kI8//tjvc/v370/Hjh2ZNGkSp59+OtOnT8/zGNd1/T7Xdd18VxBr0aIFn332GV27di3QKmO5H5P7+1eQGPx9fyONEkciIiIiIiIiIXa4yqBQOOecc3jggQdIS0ujfPnyrF69mpIlS7J582YqVqxIQkICixYt4vvvvy/yMRYtWkRWVhaVK1cmIyNj3/Z77rmHNm3aHLKKaenSpSQnJ5OcnMx3333HokWLqFWrFlu3bt33mNatW+Pz+TjrrLNYvHgxK1asoG7dunTo0IGXX36Ztm3b7mtVy6k6evTRRxk0aBA333wzL730Up7jZmdn8/7773PllVfy1ltv0bJly0N+jUcccQQ1a9ZkwoQJXHzxxezatYusrKx8v79HH310Yb+NnlLiSERERERERCQGdejQgd9//53mzZsDNhT6zTff5Nxzz+Xll1+mUaNG1K1bd19rW0HlzDgCq7oZN24cJUqUOOAxDRo0OOxqasOHD2fGjBmUKFGCk08+mfPOO4+4uDji4+Np3Lgx3bt35+abb6Z3794kJycTHx/P2LFjKV26ND169GDx4sU0atSIkiVL0rNnT2699dYD9n399dfTt29fnn766QOOW65cORYuXEizZs048sgjeeeddw77Nb/xxhvceOONPPjgg5QsWZL33nsv3+9vpCWOnPxKqsJRamqqmzN5XURERERERCSS/P7779SvX9/rMOQwypcvz7Zt27wOI2j8/Rw6jjPHdd1Uf4+PC0lUIiIiIiIiIiIScZQ4EhERERERERHZK5qrjYpCiSMREREREREREfFLiSMREREREREREfFLiSMRESkynw+SkiAuzm59Pq8jEhERERGRQIr3OgAREYlMPh/06gUZGfb58uX2OUBamndxiYiIiIhI4KjiSEREimTgwP1JoxwZGbZdRERERKLfl19+yQUXXADARx99xJNPPpnvY//77z9efPHFQh/j4YcfZujQoYfc3r17d4477jiaNGlCvXr1eOSRR/Y9rm3bttSuXRvXdfdtu/jiiylfvnyBYxg+fDgZB7/xLWb8RbFmzRouu+yygOyrMJQ4EhGRIlmxonDbRURERCQyZGVlFfo5nTp1on///vneX9TEUUENGTKEuXPnMnfuXMaNG8eyZcv23XfUUUfx7bff7ovj77//LtS+i5M4CpTMzExq1KjB+++/H/JjK3EkIiJFUrt24baLiIiIiLfS09OpV68e3bp1o1GjRlx22WX7EiJJSUk8+uijtGzZkvfee4+pU6fSvHlzUlJS6NKly74l6idPnky9evVo2bIlH3zwwb59jx07lltvvRWAtWvX0rlzZxo3bkzjxo2ZNWsW/fv3Z+nSpTRp0oR7770XsGTPKaecQqNGjXjooYf27Wvw4MHUrVuXdu3a8ccffxTqa9y5cycA5cqV27ftyiuvZPz48QB88MEHXHLJJX6fu337djp27Ejjxo1p2LAh77zzDiNGjGDNmjWceeaZnHnmmQC8/fbbJCcn07BhQ/r167fv+ZMnTyYlJYXGjRtz9tln59n/qFGjOO+889ixY8cB27t3707v3r1p1aoVJ510Ep988sm+72mXLl248MIL6dChA+np6TRs2BCw5F6fPn1ITk6mUaNGPPfccwDMmTOHNm3a0KxZM84555xCJ8n80YwjEREpksGDoXt3yMzcv61ECdsuIiIiIuHpjz/+4NVXX6VFixZcf/31vPjii/Tp0weAMmXKMHPmTDZs2MAll1zC9OnTKVeuHE899RT/93//R9++fenZsydffPEFJ554IldccYXfY9x+++20adOGDz/8kKysLLZt28aTTz7JggULmDt3LgBTp05lyZIl/Pjjj7iuS6dOnfj6668pV64c48eP55dffiEzM5OUlBSaNWt22K/r3nvv5bHHHuPPP//k9ttv5+ijj95339lnn03Pnj3Jyspi/PjxjBw5kkGDBuXZx+TJk6lRowaffvopAJs3b+bII4/k//7v/5gxYwZVqlRhzZo19OvXjzlz5lCxYkU6dOjAhAkTaNGiBT179uTrr7/muOOOY9OmTQfs+/nnn2fq1KlMmDCB0qVL5zl2eno6X331FUuXLuXMM8/kzz//BOC7775j/vz5VKpUifT09H2PHzlyJMuWLeOXX34hPj6eTZs2sWfPHm677TYmTpxI1apVeeeddxg4cCBjxow57PfvUJQ4EhGRIrnqKrjjDti+HXbtgiOPhP/+gyOO8DoyERERkQhw552wN4kSME2awPDhh3xIrVq1aNGiBQBXX301I0aM2Jc4ykkEff/99/z222/7Hrd7926aN2/OokWLOO6446hTp86+548cOTLPMb744gtef/11AEqUKMGRRx7Jv//+e8Bjpk6dytSpU2natCkA27ZtY8mSJWzdupXOnTuTkJAAWAtcQQwZMoTLLruMbdu2cfbZZzNr1izOOOOMfTG0bNmSd955hx07dpCUlOR3H8nJyfTp04d+/fpxwQUX0KpVqzyP+emnn2jbti1Vq1YFIC0tja+//poSJUrQunVrjjvuOAAqVaq07zlvvPEGNWvWZMKECZQsWdLvsS+//HLi4uKoU6cOxx9/PIsWLQKgffv2B+wrx/Tp0+nduzfx8fH7jrdgwQIWLFhA+/btAatKql69ekG+fYekVjURESmSb7+FjRth1CjIzoZ166BBA7jtNksmiYiIiEj4cRwn389z2rtc16V9+/b7Zgb99ttvvPrqq36fX1Su6zJgwIB9x/jzzz+54YYbin2M8uXL07ZtW2bOnHnA9iuvvJLbbruNyy+/PN/nnnTSScyZM4fk5GQGDBjAo48+6jfu/L6e/OJu2LAh6enprFq1Kt9j5/f/krvl7nDHc12XBg0a7Pue/vrrr0ydOjXfYxaUEkciIlIkPh8kJMDFF9vnJUvCSy/B8uXgp/JXRERERHIbPhy+/DKw/w5TbQSwYsUKvvvuO8Bm9bRs2TLPY04//XS+/fbbfe1SGRkZLF68mHr16rFs2TKWLl267/n+nH322bz00kuAVb1s2bKFChUqsHXr1n2POeeccxgzZsy+2UmrV69m3bp1tG7dmg8//JAdO3awdetWPv7448N+TbllZmbyww8/cMIJJxywvVWrVgwYMICrrroq3+euWbOGhIQErr76avr06cPPP/8McEDsp512Gl999RUbNmwgKyuLt99+mzZt2tC8eXO++uqrfUO5c7eqNW3alFdeeYVOnTqxZs0av8d+7733yM7OZunSpfz111/UrVv3kF9nhw4dePnll8ncOzdi06ZN1K1bl/Xr1+/7/92zZw8LFy485H4KQokjEREptN274d134aKLIPdKpq1awfXXw7BhsGCBd/GJiIiIiH/169dn3LhxNGrUiE2bNnHTTTfleUzVqlUZO3YsV111FY0aNeL0009n0aJFlClThpEjR9KxY0datmxJYmKi32M8++yzzJgxg+TkZJo1a8bChQupXLkyLVq0oGHDhtx777106NCBrl270rx5c5KTk7nsssvYunUrKSkpXHHFFTRp0oRLL73Ub7uYP/feey9NmjShUaNGJCcn5xmA7TgOffr0oUqVKvnu49dff+XUU0+lSZMmDB48mPvvvx+AXr16cd5553HmmWdSvXp1nnjiCc4880waN25MSkoKF110EVWrVmXkyJFccsklNG7cOM/8p5YtWzJ06FA6duzIhg0b8hy7bt26tGnThvPOO4+XX36ZMmXKHPLr7dGjB7Vr16ZRo0Y0btyYt956i1KlSvH+++/Tr18/GjduTJMmTZg1a1aBvn+H4uRXZhWOUlNT3dmzZ3sdhohIzJs40SqNPv0Uzj//wPs2bIB69aB+ffjqK4jTJQoRERERAH7//Xfq16/v2fHT09O54IILWKArfGGle/fuXHDBBVx22WUhOZ6/n0PHcea4rpvq7/F6Oy8iIoXm80GVKrB37t4BqlSBIUNg5kx47bXQxyYiIiIi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jkTkQKNGQb160LKl15FIKDVpAsccozlHIiIiIhI7lDiSsNahg91Om+ZtHCK5/fqrDW7XUOzYExdn7WpTptgMNhERERGRaKfEkYS1evWgZk21q0l48PkgKQkaNbLPExI8DUc8cv75sHkzzJrldSQiIiIiIsGnxJGENcexqqPp0yEry+toJJb5fDbPaPny/dvuuce2S2xp3x7i47W6moiIiIjEBiWOJOx16AD//QezZ3sdicSygQMhI+PAbRkZtl1iyxFHQKtWmnMkIiIiIrFBiSMJe2efbZVHalcTL61YUbjtEt06doQFC/T/LyIiIiLRT4kjCXtVqkCzZkocibdq1y7cdolu559vt2pXExEREZFod9jEkeM4YxzHWec4zoJc2wY5jjPfcZy5juNMdRynxt7tpRzHec1xnF8dx5nnOE7bfPZZyXGcaY7jLNl7WzFQX5BEp/btbRWrLVu8jiS25AyDjouz21ie5zN4MJQufeC2hATbLrGnXj047jgljkREREQk+hWk4mgscO5B24a4rtvIdd0mwCfAg3u39wRwXTcZaA8McxzH3zH6A5+7rlsH+Hzv5yL56tDBhmPPmOF1JLEj9zBo17XbXr1iN3mUlgYXXLD/88REGDnStkvscRyrOvr8c9i50+toRERERESC57CJI9d1vwY2HbQtd91HOcDd+/HJWCII13XXAf8BqX52exEwbu/H44CLCxGzxKDmzaFcObWrhZKGQee1ejWceqol0tLTlTSKdR072u/EV195HYmIiIiISPAUecaR4ziDHcdZCaSxv+JoHnCR4zjxjuMcBzQDavl5ejXXdf8G2Ht7dFHjkNhQujS0bavEUSjlN/R3+XL46CPYvTu08Xhtwwb44Qc47zyvI5Fw0bYtlC2r1dVEREREJLoVOXHkuu5A13VrAT7g1r2bxwCrgNnAcGAWkFmcAB3H6eU4zmzHcWavX7++OLuSCNehA/z5Jyxb5nUkseGYY/xvj4uDiy6C6tXhpptg5kzIzg5tbF6YOtUqjXKGIouULQtnnWWJI9c9/ONFRERERCJRIFZVewu4FMB13UzXde9yXbeJ67oXAUcBS/w8Z63jONUB9t6uy2/nruuOdF031XXd1KpVqwYgXIlUHTrY7bRp3sYRC1wXKlfOuz0hAcaMsRPlc86BceOgVSs4/nhrYfvtt9DHGiqTJtkKf6n+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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt \n",
    "indices = np.arange(0, 60)\n",
    "fig, ax = plt.subplots(1,1,figsize = (20, 10))\n",
    "plt.plot(y_test_reshaped[:60], color = \"blue\", label = \"real IBM stock price\")\n",
    "plt.scatter(indices, y_test_reshaped[:60], color = \"blue\")\n",
    "plt.plot(predictions[:60], color = \"red\", label = \"predicted IBM stock price\")\n",
    "plt.scatter(indices, predictions[:60], color = \"red\")\n",
    "plt.legend()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# look for literature which suggests the accuracy is ~50%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# utilizing other indicators besides opening price may affect accuracy "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
