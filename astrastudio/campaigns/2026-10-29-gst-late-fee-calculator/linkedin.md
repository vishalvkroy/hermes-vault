₹200. That's the late fee alone on a GSTR-3B filed just 4 days late, before 18% annual interest on the tax itself even starts counting.

Last week three different merchants asked our support WhatsApp the same question, almost word for word: what's my actual due date, and what happens if I miss it. Every GST billing tool I checked treats this like a once-a-year lookup. It isn't. It's a question every single filing cycle, for every GSTIN in the country, forever.

So we built a calculator and put it on the website for free, no login:

- Pick GSTR-1 or GSTR-3B, monthly or QRMP
- It works out the real due date from the actual filing rule - 11th for monthly GSTR-1, 20th for monthly GSTR-3B, 13th/22nd/24th for QRMP - never a hardcoded date that quietly goes wrong next quarter
- Enter how many days late and your turnover slab, and it gives the exact late fee (₹50/day split CGST+SGST, ₹20/day for nil returns, capped between ₹2,000 and ₹10,000 by turnover) plus 18% p.a. interest on the tax you actually owed in cash

Every number was checked against current CBIC guidance before it shipped. One thing we deliberately left out: which states count as Category X vs Category Y for QRMP due dates. That classification can change, and a wrong hardcoded list costs someone more than no list at all - it's a toggle with a note to verify on the portal instead.

Most billing software stops at "here's your invoice." The part that actually costs small business owners money is the two weeks after - not knowing the real deadline, then getting hit with a fee that compounds for every day it sits unpaid.

It's live at astrastudio.in/tools/gst-late-fee-calculator.

What's the one GST question your accountant gets asked every single filing cycle?
