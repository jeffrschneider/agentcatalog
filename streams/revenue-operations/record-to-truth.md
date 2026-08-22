# Value stream: Record-to-Truth

`vs/rev/record-to-truth v1`

**position:** 2
A run starts whenever records arrive from somewhere: a form, an import, an
enrichment feed, a person typing. The processes here decide what a record
must contain before it is usable, deduplicate it against what is already
held, enrich what is thin, correct what is wrong, and keep the definitions
everything else counts against. This is the stream that decides whether an
account means the same thing in two reports and whether a number can be
trusted twice. It owns the shape of the record and the rules that keep it
honest; what anybody does with a record belongs to whoever is doing it.
