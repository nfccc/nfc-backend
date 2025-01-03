from django.shortcuts import render

def track_nfc_tag(request, tag_id):
    """
    This view handles requests with a TAGID passed in the URL.
    """
    # Log or process the received NFC Tag ID (TAGID)
    print(f"Received NFC Tag ID: {tag_id}")
    
    # Prepare the context for the template
    context = {
        'status': 'success',
        'tag_id': tag_id,
        'message': 'Tag ID received successfully'
    }
    
    # Render the HTML template with the context data
    return render(request, "tag.html", context)
