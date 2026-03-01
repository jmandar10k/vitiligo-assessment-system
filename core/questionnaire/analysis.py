# 1) vitiligo Type analysis 

def determine_vitiligo_type(responses: dict) -> str:

    vitiligo_types = set()

    # Face
    if 'at the openings(lips/nostrils/ears)' in responses.get('face', []):
        vitiligo_types.add(
            'Acrofacial vitiligo (due to spots on the face openings).'
        )

    if 'on one side of the face' in responses.get('face', []):
        vitiligo_types.add(
            'Segmental vitiligo (due to spots on one side of the face).'
        )

    if 'on both sides of the face' in responses.get('face', []):
        vitiligo_types.add(
            'Non-segmental vitiligo (due to spots on both sides of the face).'
        )

    if 'just one spot on face' in responses.get('face', []):
        vitiligo_types.add(
            'Focal vitiligo (due to a single spot on the face).'
        )

    # Hands & Feet
    if 'at the ends of limbs(fingers / toes)' in responses.get('hands_feet', []):
        vitiligo_types.add(
            'Acrofacial vitiligo (due to spots on the fingers).'
        )

    if 'on both hands or feet' in responses.get('hands_feet', []):
        vitiligo_types.add(
            'Non-segmental vitiligo (due to spots on both hands or feet).'
        )

    if 'on only one hand or feet' in responses.get('hands_feet', []):
        vitiligo_types.add(
            'Segmental vitiligo (due to spots on only one hand or foot).'
        )

    # Arms & Legs
    if 'on both arms or legs' in responses.get('arms_legs', []):
        vitiligo_types.add(
            'Non-segmental vitiligo (due to spots on both arms or legs).'
        )

    if 'on only one arm or leg' in responses.get('arms_legs', []):
        vitiligo_types.add(
            'Segmental vitiligo (due to spots on only one arm or leg).'
        )

    # Whole Body
    if 'yes' in responses.get('whole_body', []):
        vitiligo_types.add(
            'Universal vitiligo (depigmentation over 80% of the body).'
        )

    if vitiligo_types:
        return ", ".join(vitiligo_types)

    return "Unknown type"

# 2) insight and conclusion vitiligo progression

def generate_insights_and_conclusion(
    white_patches,
    patch_shape,
    expanding_patches,
    patch_duration,
    sensations,
    color_change,
    new_patches,
    visibility_in_sunlight
):

    insights = []

    if white_patches == "Yes":

        insights.append(
            "1) The patient has white patches, suggesting possible depigmentation-related conditions like vitiligo."
        )

        if patch_shape == "Irregular":
            insights.append(
                "2) Irregular shapes may indicate active, progressive vitiligo."
            )
        elif patch_shape in ["Round", "Oval"]:
            insights.append(
                "2) Round/oval shapes may indicate more stable vitiligo patches."
            )
        else:
            insights.append(
                "2) Patch shape unclear; further observation recommended."
            )

        if expanding_patches == "Yes, they are growing":
            insights.append(
                "3) Patches are progressing and spreading."
            )
        elif expanding_patches == "No, they have remained the same size":
            insights.append(
                "3) The vitiligo appears stable."
            )
        else:
            insights.append(
                "3) Expansion status uncertain; monitoring required."
            )

        if patch_duration in ["6-12 months", "More than 1 year"]:
            insights.append(
                "4) Chronic condition with prolonged presence."
            )
        elif patch_duration in ["Less than 3 months", "3-6 months"]:
            insights.append(
                "4) Recent onset; may indicate early-stage vitiligo."
            )

        if sensations == "No, no sensations":
            insights.append(
                "5) Lack of sensory symptoms aligns with typical vitiligo."
            )
        else:
            insights.append(
                f"5) Presence of {sensations} may require differential diagnosis."
            )

        if color_change == "Yes, they have lightened over time":
            insights.append(
                "6) Progressive depigmentation observed."
            )
        else:
            insights.append(
                "6) No major color progression reported."
            )

        if new_patches == "Yes, within the last 3 months":
            insights.append(
                "7) Active disease with new patch formation."
            )
        else:
            insights.append(
                "7) No new patches suggest stability."
            )

        if visibility_in_sunlight == "Yes, they are more noticeable":
            insights.append(
                "8) Sunlight contrast supports vitiligo diagnosis."
            )

    else:
        insights.append(
            "No white patches detected; vitiligo unlikely."
        )

    # Conclusion logic
    conclusion = ""

    if white_patches != "Yes":
        conclusion = "Based on responses, vitiligo is unlikely."
        return insights, conclusion

    progressive = (
        expanding_patches == "Yes, they are growing"
        or new_patches == "Yes, within the last 3 months"
    )

    if progressive:
        conclusion = "The condition appears progressive and active."
    else:
        conclusion = "The condition appears stable."

    if sensations == "No, no sensations":
        conclusion += " Absence of sensory symptoms aligns with vitiligo."

    if visibility_in_sunlight == "Yes, they are more noticeable":
        conclusion += " Sunlight contrast further supports depigmentation."

    return insights, conclusion