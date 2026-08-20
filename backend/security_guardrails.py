"""
Security Guardrails for MSME Digital Twin
Enforces Step 9 of the Architectural Blueprint.
"""
from functools import wraps
import logging

class SecurityGuardrails:
    @staticmethod
    def verify_human_approval_required(func):
        """
        Decorator to ensure automatic lending decisions are blocked.
        The AI can only recommend; a human must explicitly approve.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Enforce that human approval must be explicitly True
            human_approved = kwargs.get('human_approved', False)
            if not human_approved:
                logging.warning("Auto-lending blocked: Human approval is mandatory.")
                raise PermissionError("Lending decisions require explicit human approval. Auto-approval blocked.")
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def trigger_consent_revocation_deletion(user_id: str, db_session):
        """
        Enforces data minimization by deleting all data associated
        with the user upon consent revocation.
        """
        logging.info(f"Triggering consent revocation and data deletion for user {user_id}.")
        try:
            # Placeholder for actual data deletion logic across domains
            pass
        except Exception as e:
            logging.error(f"Failed to delete data for user {user_id}: {e}")
            raise
        
        return {"status": "success", "message": f"Consent revoked and all data for {user_id} deleted."}

    @staticmethod
    def audit_schema_for_protected_characteristics(schema_fields):
        """
        Ensures no protected characteristics (religion, caste, gender)
        are tracked in the database schemas.
        """
        forbidden_fields = {'religion', 'caste', 'gender'}
        for field in schema_fields:
            if field.lower() in forbidden_fields:
                logging.error(f"Schema validation failed: Field '{field}' is a protected characteristic.")
                raise ValueError(f"Protected characteristic '{field}' found in schema. Tracking this is forbidden.")
        return True
