import { Router } from 'express';

const router = Router();

router.get('/', (req, res) => {
    res.send({type:'request headers', headers: req.headers});
})

export default router;