import javalang

def identify_entities(java_code):

    # Dummy class name
    class_name = "xyz" 
    java_code = "class "+class_name.split('.')[-1]+" {" + java_code + "}"
    
    # Helper functions to add entities with their positions
    def add_class(node):
        entities.append({
            "entity_name": node.name,
            "entity_type": "CLASS",
            "position": (node.position.line, node.position.column) if node.position else None
        })
        

    
    def add_method(node):
        entities.append({
            "entity_name": node.name,
            "entity_type": "FUNCTION",
            "position": (node.position.line, node.position.column) if node.position else None
        })
        
    
    def add_variable(node, type_node, position):
        entities.append({
            "entity_name": node.name,
            "entity_type": "VARIABLE",
            "position": position
        })
        
    
    def add_value(node):
        entities.append({
            "entity_name": node.value,
            "entity_type": "VALUE",
            "position": (node.position.line, node.position.column) if node.position else None
        })
        

    
    def add_data_type(node):
        if isinstance(node, javalang.tree.ReferenceType):
            entities.append({
            "entity_name": node.name,
            "entity_type": "DATA TYPE",
            "position": (node.position.line, node.position.column) if node.position else None
        })

    def add_library(node):
        entities.append({
            "entity_name": node.name,
            "entity_type": "LIBRARY",
            "position": (node.position.line, node.position.column) if node.position else None
        })
        
    entities = []

    # Parse the Java code using javalang
    tokens = list(javalang.tokenizer.tokenize(java_code))
    parser = javalang.parser.Parser(tokens)
    wc = 0

    try:
        tree = parser.parse()
    
                
        
        # Visit nodes in the AST
        for path, node in tree:
            if isinstance(node, javalang.tree.ClassDeclaration):
                add_class(node)
                
            elif isinstance(node, javalang.tree.MethodDeclaration):
                add_method(node)
                
            elif isinstance(node, javalang.tree.VariableDeclarator):
                variable_declaration = path[-2]  # VariableDeclarator is within VariableDeclaration
                type_node = variable_declaration.type.name if isinstance(variable_declaration.type, javalang.tree.ReferenceType) else str(variable_declaration.type)
                add_variable(node, type_node, (variable_declaration.position.line, variable_declaration.position.column) if variable_declaration.position else None)
                
            elif isinstance(node, javalang.tree.Literal):
                add_value(node)
                
            elif isinstance(node, javalang.tree.Import):
                add_library(node)
               
            elif isinstance(node, javalang.tree.ReferenceType):
                add_data_type(node)

    except javalang.parser.JavaSyntaxError as err:
        wc  = wc + 1
        print("syntax error on: "+str(err))
    except javalang.tokenizer.LexerError as err:
        wc = wc + 1
        print("lexer error on: " +code_copy)
    except IndexError as e:
        wc = wc + 1
    except TypeError as e:
        wc = wc + 1
    
    return entities[1:], wc
