from __future__ import annotations


def stable_matching(
    donor_pref: list[list[int]], recipient_pref: list[list[int]]
) -> list[int]:
    assert len(donor_pref) == len(recipient_pref)

    n = len(donor_pref)
    unmatched_donors = list(range(n))
    donor_record = [-1] * n  
    rec_record = [-1] * n  
    num_donations = [0] * n

    while unmatched_donors:
        donor = unmatched_donors[0]
        donor_preference = donor_pref[donor]
        recipient = donor_preference[num_donations[donor]]
        num_donations[donor] += 1
        rec_preference = recipient_pref[recipient]
        prev_donor = rec_record[recipient]

        if prev_donor != -1:
            if rec_preference.index(prev_donor) > rec_preference.index(donor):
                rec_record[recipient] = donor
                donor_record[donor] = recipient
                unmatched_donors.append(prev_donor)
                unmatched_donors.remove(donor)
        else:
            rec_record[recipient] = donor
            donor_record[donor] = recipient
            unmatched_donors.remove(donor)
    return donor_record
