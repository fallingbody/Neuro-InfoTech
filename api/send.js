export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const data = req.body;
    
    // Construct the email body from the form fields
    const emailBody = Object.entries(data)
      .map(([key, value]) => `<strong>${key}:</strong> ${value}`)
      .join('<br>');

    // Send the email using Resend API directly via fetch
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: 'Acme <onboarding@resend.dev>', // Resend's testing domain
        to: 'itzksv@gmail.com', // Your email address
        subject: 'New Contact Form Submission',
        html: `<p>You received a new submission from your website:</p><p>${emailBody}</p>`
      })
    });

    const result = await response.json();
    return res.status(200).json(result);
  } catch (error) {
    console.error('Error sending email:', error);
    return res.status(500).json({ error: 'Failed to send email' });
  }
}
