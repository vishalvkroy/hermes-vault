A retailer selling Coke and carbonated water couldn't bill correctly in our software. Not a small bug: their goods carry 28% GST plus 12% Compensation Cess, and our rate list stopped at 28%.

The tempting fix is obvious: add a 40% slab and move on. We didn't, because there's no 40% GST rate in India. Filing it that way would overstate GST owed and report zero cess, and cess input credit can only offset cess output, never GST. Merge the two into one number and the monthly tax payable comes out wrong every time.

So cess now travels alongside GST through the entire flow: product setup, sale, purchase, invoice, return, and the GSTR-1 filing. It gets its own ledger accounts. Never touches the GST ones.

Building this surfaced two bugs testing caught before any customer did:
- Cess was being added up per line item but never rolled into the sale total, so the receipt read one number and our books recorded another.
- The purchase side had nowhere to record cess paid coming in, so retailers had no way to claim the input credit they were owed, and their liability looked higher than it actually was.

1,162 tests passing before we shipped it. That number matters more to me than any dashboard we've built this year.

This is the boring part of building GST-compliant software for Indian retailers: shop owners selling soft drinks or tobacco deal with rules most POS tools weren't built to handle at all. If your current billing software rounds this off with "just add it to GST," ask what it's doing with the cess input credit you're not claiming.

#buildinpublic #IndianSMB #GST #POS #Fintech
