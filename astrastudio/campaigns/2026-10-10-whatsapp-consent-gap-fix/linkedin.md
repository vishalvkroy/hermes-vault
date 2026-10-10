One screen in Astra Atlas's POS has two ways to add a customer: type in a new one, or search for an existing one.

For months, only the first path asked for WhatsApp-marketing consent. Pick an existing customer from search instead, and the consent checkbox never appeared. Not hidden behind a toggle. Missing from that code branch.

Every shop using Spark (our WhatsApp CRM) to message customers already on file was doing it without a consent record for anyone added that second way. A real gap under India's DPDP Act, not a theoretical one.

We caught it in an internal audit, not a complaint. Fixed it 3 October: the checkbox now shows on both paths, gated so it only asks people who haven't already said yes.

Billing-software comparisons in this market argue about sync speed and WhatsApp reminders as a selling point. None of them mention what happens to consent once it's collected, or whether it gets collected on every path a shopkeeper actually uses.

That is the unglamorous part of building compliance into software. It is never the feature you demo. It is the code path nobody re-checks after the first release.

What's the last bug your team caught by auditing your own product, before anyone complained about it?

P.S. Same commit also added a new-device login alert for every account - a separate fix, same audit pass.

#BuildInPublic #IndianSMB
