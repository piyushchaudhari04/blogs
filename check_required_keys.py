def verify_required_keys(logger):
    def decorate(f):
        def applicator(*args, **kwargs):
            missing_valid_keys = set(valid_keys) - set(kwargs.keys())
            if len(missing_valid_keys) != 0:
                error_msg = (f'Missing required keys - {', '.join(map(str, list(missing_valid_keys)}')))
                result = {'error': error_msg, 'status_code': 400}
            else:
                result = f(*args, **kwargs)
            return result
        return applicator
    return decorate

@verify_required_keys(["text","lang"])                                                        
def predict(text, lang):
    model = get_model()
    prediction = model.predict(text, lang)
    return prediction                                                    
