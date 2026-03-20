#!/usr/bin/env python3
"""
Feature: Display Current Hijri Date
This script shows the current date in the Islamic (Hijri) calendar.
"""

from datetime import datetime
try:
    from hijri_converter import Hijri, Gregorian
except ImportError:
    print("Error: hijri-converter library not found.")
    print("Install it using: pip install hijri-converter")
    exit(1)


def get_hijri_date():
    """
    Get the current date in Hijri calendar format.
    
    Returns:
        str: Formatted Hijri date string
    """
    today = datetime.now()
    
    # Convert Gregorian date to Hijri
    hijri_date = Gregorian(today.year, today.month, today.day).to_hijri()
    
    # Format the date nicely
    hijri_months = [
        "Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-thani",
        "Jumada al-awwal", "Jumada al-thani", "Rajab", "Sha'ban",
        "Ramadan", "Shawwal", "Dhu al-Qi'dah", "Dhu al-Hijjah"
    ]
    
    month_name = hijri_months[hijri_date.month - 1]
    
    return f"{hijri_date.day} {month_name} {hijri_date.year} AH"


if __name__ == "__main__":
    print("=" * 50)
    print("Current Hijri Date")
    print("=" * 50)
    
    gregorian = datetime.now()
    hijri = get_hijri_date()
    
    print(f"Gregorian Date: {gregorian.strftime('%A, %B %d, %Y')}")
    print(f"Hijri Date:     {hijri}")
    print("=" * 50)
